# Play-Annotation-Generator Annotation Review — Post10to15_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_65`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Fum`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 81
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `16` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 20 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 8 | START | 8 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 11 | START | 22 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `15` | `15` | 11 | START | 11 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 11 | START | 11 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `20` | `20` | 11 | START | 11 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 11 | START | 11 | 18 |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | `7` | `7` | 21 | START | 21 | 180 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 21 | END | 8 | 21 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 76 | START | 76 | 82 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_SnapReceive` | 8 | 21 | 14 | inferred_complete_timeline |
| `Action_None` | 22 | 75 | 54 | inferred_complete_timeline |
| `Action_ThrowPass` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_None` | 83 | 131 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunPostRoute` | 21 | 180 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 128 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 57 | 50 | inferred_complete_timeline |
| `Action_None` | 65 | 70 | 6 | inferred_complete_timeline |
| `Action_None` | 72 | 99 | 28 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 154 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 78 | 68 | inferred_complete_timeline |
| `Action_PassBlock` | 80 | 81 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 100 | 90 | inferred_complete_timeline |
| `Action_PassBlock` | 115 | 141 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_BallSnap` | 8 | 21 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 22 | 28 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 34 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 55 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 127 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 18 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 21 | 26 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 40 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 74 | 25 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 124 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 149 | 168 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 11 | 36 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 180 | 50 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 43 | 36 | inferred_complete_timeline |
| `Action_None` | 54 | 62 | 9 | inferred_complete_timeline |
| `Action_None` | 66 | 101 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 52 | 45 | inferred_complete_timeline |
| `Action_None` | 84 | 126 | 43 | inferred_complete_timeline |
| `Action_None` | 128 | 130 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 80 | 73 | inferred_complete_timeline |
| `Action_None` | 82 | 156 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 141 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 106 | 180 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 126 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 180 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 81 | 74 | inferred_complete_timeline |
| `Action_None` | 94 | 106 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 141 | 134 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 40–141 | 97 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 67–141 | 71 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 86–141 | 56 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 96–119 | 24 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 126–128 | 3 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 142–180 | 39 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 142–146 | 5 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 147–180 | 29 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 153–180 | 28 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 173–180 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (7 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [8–21], lower_priority='Action_PassBlock' annotated_start=11, effective_Action_PassBlock_start=22.
- ⚠️ Action 'Action_None' range [8-52] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-126] for track '0' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-43] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-62] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-94] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-141] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [21-180] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-156] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-81] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-106] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [22-28] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-34] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-55] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-78] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [80-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-99] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [115-141] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-36] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [11-18] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [21-26] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-40] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-74] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-124] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [149-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-43] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-141] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-80] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-141] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-141] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-119] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-157] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-180] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>
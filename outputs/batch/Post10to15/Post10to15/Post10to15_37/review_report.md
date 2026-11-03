# Play-Annotation-Generator Annotation Review — Post10to15_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_37`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 78
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR4 | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `10` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 9 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `19` | `19` | 10 | START | 10 | 13 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `14` | `14` | 13 | START | 13 | 84 |
| ✅ EXACT | `Action_PassBlock` | LT | `16` | `16` | 13 | START | 13 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 13 | START | 13 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 13 | START | 29 | 133 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 13 | START | 13 | 28 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR4 | `0` | `0` | 28 | START | 28 | 123 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 28 | END | 10 | 28 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 75 | START | 75 | 84 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 28 | 19 | inferred_complete_timeline |
| `Action_None` | 29 | 74 | 46 | inferred_complete_timeline |
| `Action_ThrowPass` | 75 | 84 | 10 | inferred_complete_timeline |
| `Action_None` | 85 | 180 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 17 | 122 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 122 | 113 | inferred_complete_timeline |
| `Action_None` | 124 | 144 | 21 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 163 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_RunPostRoute` | 28 | 123 | 96 | inferred_complete_timeline |
| `Action_RunPostRoute` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_RunPostRoute` | 140 | 142 | 3 | inferred_complete_timeline |
| `Action_RunPostRoute` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_RunPostRoute` | 168 | 180 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 117 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 32 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 35 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 13 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 19 | 24 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 28 | 28 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 133 | 105 | inferred_complete_timeline |
| `Action_PassBlock` | 139 | 171 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 180 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–28
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 28 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 84 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 180 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 113 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 108 | 99 | inferred_complete_timeline |
| `Action_None` | 113 | 180 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 100 | 91 | inferred_complete_timeline |
| `Action_None` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_None` | 117 | 145 | 29 | inferred_complete_timeline |
| `Action_None` | 153 | 180 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 169 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 21–180 | 159 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 51–52 | 2 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 58–100 | 16 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 59–117 | 11 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 125–180 | 47 | 6 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 130–180 | 49 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 149–180 | 32 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 168–172 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `0` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [10–28], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=29.
- ⚠️ Action 'Action_RunPostRoute' range [28-123] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [130-134] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [140-142] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [154-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [168-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-113] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-145] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-113] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-163] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-108] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-144] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-117] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [34-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [10-13] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [19-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-133] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [139-171] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-28] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-122] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-143] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-68] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-62] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-180] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-172] for track '29' has 1 frames without a visible bounding box.
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

</details>
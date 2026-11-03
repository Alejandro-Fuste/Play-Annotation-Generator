# Play-Annotation-Generator Annotation Review — Slants0to10_75

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_75`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 19 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 9 | START | 9 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 20 | START | 26 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 20 | START | 20 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 20 | START | 26 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `7` | `7` | 20 | START | 20 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 20 | START | 20 | 21 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `1` | `1` | 20 | START | 20 | 88 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 23 | END | 9 | 23 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 60 | START | 60 | 69 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `1` | 94 | START | 94 | 239 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 23 | 15 | inferred_complete_timeline |
| `Action_None` | 24 | 59 | 36 | inferred_complete_timeline |
| `Action_ThrowPass` | 60 | 69 | 10 | inferred_complete_timeline |
| `Action_None` | 70 | 113 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 133 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 121 | 113 | inferred_complete_timeline |
| `Action_None` | 127 | 239 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 20 | 88 | 69 | inferred_complete_timeline |
| `Action_None` | 89 | 93 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 239 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 188 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 21 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 27 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 123 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 77 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 9 | 21 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 54 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 78 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 125 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 20 | 1 | inferred_complete_timeline |
| `Action_PassBlock` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 239 | 211 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 20 | 12 | inferred_complete_timeline |
| `Action_None` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_None` | 29 | 37 | 9 | inferred_complete_timeline |
| `Action_None` | 42 | 44 | 3 | inferred_complete_timeline |
| `Action_None` | 55 | 159 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 21 | 13 | inferred_complete_timeline |
| `Action_None` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_None` | 29 | 74 | 46 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 126 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 21 | 13 | inferred_complete_timeline |
| `Action_None` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_None` | 29 | 40 | 12 | inferred_complete_timeline |
| `Action_None` | 44 | 192 | 149 | inferred_complete_timeline |
| `Action_None` | 194 | 235 | 42 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 22 | 14 | inferred_complete_timeline |
| `Action_None` | 26 | 46 | 21 | inferred_complete_timeline |
| `Action_None` | 48 | 65 | 18 | inferred_complete_timeline |
| `Action_None` | 69 | 76 | 8 | inferred_complete_timeline |
| `Action_None` | 82 | 86 | 5 | inferred_complete_timeline |
| `Action_None` | 88 | 128 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 66 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 21 | 13 | inferred_complete_timeline |
| `Action_None` | 26 | 27 | 2 | inferred_complete_timeline |
| `Action_None` | 29 | 49 | 21 | inferred_complete_timeline |
| `Action_None` | 53 | 74 | 22 | inferred_complete_timeline |
| `Action_None` | 76 | 129 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 239 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 239 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 239 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 239 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_None` | 9 | 70 | 62 | inferred_complete_timeline |
| `Action_None` | 73 | 125 | 53 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–124 | 125 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 49–115 | 66 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 57–64 | 8 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 90–129 | 36 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 95–239 | 145 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 190–239 | 50 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 76: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [9–23], lower_priority='Action_PassBlock' annotated_start=20, effective_Action_PassBlock_start=24.
- ⚠️ Action 'Action_None' range [9-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-121] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-22] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-46] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-20] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-37] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-21] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-49] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-74] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '7' starts at frame 20, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [20-20] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-27] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-21] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-27] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-40] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-70] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [9-21] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-74] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' for track '19' starts at frame 20, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PassBlock' range [20-20] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-27] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [26-27] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-78] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-78] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-64] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-108] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>
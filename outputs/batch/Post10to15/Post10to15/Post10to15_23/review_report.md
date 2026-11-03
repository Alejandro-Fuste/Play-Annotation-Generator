# Play-Annotation-Generator Annotation Review — Post10to15_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_23`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 64
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR3 | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `20` | 10 | START | 10 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `10` | `10` | 13 | START | 13 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 13 | START | 13 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 13 | START | 25 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 13 | START | 13 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `8` | `8` | 13 | START | 13 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR3 | `9` | `9` | 24 | START | 24 | 121 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 24 | END | 10 | 24 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 71 | START | 71 | 83 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_None` | 25 | 70 | 46 | inferred_complete_timeline |
| `Action_ThrowPass` | 71 | 83 | 13 | inferred_complete_timeline |
| `Action_None` | 84 | 122 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 76 | 67 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 113 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 86 | 77 | inferred_complete_timeline |
| `Action_None` | 96 | 125 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

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
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_RunPostRoute` | 24 | 121 | 98 | inferred_complete_timeline |
| `Action_RunPostRoute` | 126 | 180 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 73 | 61 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 150 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 93 | 81 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 124 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 24 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 25 | 44 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 53 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 127 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 64 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 67 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 44 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 131 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 120 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 115 | 106 | inferred_complete_timeline |
| `Action_None` | 119 | 136 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 27 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–47
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 29 | 20 | inferred_complete_timeline |
| `Action_None` | 31 | 41 | 11 | inferred_complete_timeline |
| `Action_None` | 44 | 47 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 101 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 128 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 86 | 77 | inferred_complete_timeline |
| `Action_None` | 89 | 180 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 85 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 101 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 25–34 | 10 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 28–72 | 19 | 4 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 48–50 | 3 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 67–128 | 20 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 70–135 | 33 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 80–130 | 48 | 2 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 88–120 | 33 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 100–133 | 29 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 111–179 | 64 | 3 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 122–139 | 18 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 165–180 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [10–24], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=25.
- ⚠️ Action 'Action_None' range [10-86] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-76] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-86] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-101] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-44] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-131] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [24-121] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [126-180] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-73] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-85] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-128] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-27] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-64] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-29] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-41] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-47] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-115] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-136] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [25-44] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [48-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-127] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-124] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-30] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-46] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-128] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-78] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-135] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-130] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-120] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-105] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-133] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-146] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-157] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-179] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-139] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.

</details>
# Play-Annotation-Generator Annotation Review — CrackToss_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_29`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 107
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | CB2 | defense | `4` | `3` |
| ✅ EXACT | `Action_PullBlock` | DT1 | defense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | DT2 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | DT2 | defense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 5 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | C | `17` | `16` | 6 | START | 6 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `19` | `18` | 9 | START | 9 | 34 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | CB2 | `4` | `3` | 9 | START | 9 | 44 |
| ✅ EXACT | `Action_PullBlock` | DT1 | `2` | `1` | 9 | START | 9 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | DT2 | `15` | `14` | 32 | END | 6 | 18 |
| ⚠️ AMBIGUOUS MATCH | `Action_Toss` | DT2 | `15` | `14` | 37 | START | 37 | 46 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `5` | 79 | START | 79 | 203 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 167 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_BallCarry` | 79 | 203 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 68 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 44 | 39 | inferred_complete_timeline |
| `Action_None` | 46 | 50 | 5 | inferred_complete_timeline |
| `Action_None` | 96 | 204 | 109 | inferred_complete_timeline |
| `Action_None` | 217 | 239 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_BallSnap` | 6 | 30 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 32 | 1 | inferred_complete_timeline |
| `Action_None` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_None` | 36 | 42 | 7 | inferred_complete_timeline |
| `Action_None` | 54 | 80 | 27 | inferred_complete_timeline |
| `Action_None` | 86 | 108 | 23 | inferred_complete_timeline |
| `Action_None` | 110 | 172 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 44 | 39 | inferred_complete_timeline |
| `Action_None` | 76 | 203 | 128 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 30 | 25 | inferred_complete_timeline |
| `Action_None` | 36 | 70 | 35 | inferred_complete_timeline |
| `Action_None` | 72 | 92 | 21 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 116 | 122 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 48 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 9 | 18 | 10 | inferred_complete_timeline |
| `Action_None` | 19 | 239 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_SnapReceive` | 6 | 18 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 20 | 32 | 13 | inferred_complete_timeline |
| `Action_None` | 33 | 36 | 4 | inferred_complete_timeline |
| `Action_Toss` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_Toss` | 52 | 78 | 27 | inferred_complete_timeline |
| `Action_None` | 79 | 144 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 102 | 97 | inferred_complete_timeline |
| `Action_None` | 108 | 156 | 49 | inferred_complete_timeline |
| `Action_None` | 160 | 239 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 73 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_CrackBlock` | 9 | 44 | 36 | inferred_complete_timeline |
| `Action_CrackBlock` | 50 | 66 | 17 | inferred_complete_timeline |
| `Action_CrackBlock` | 86 | 116 | 31 | inferred_complete_timeline |
| `Action_CrackBlock` | 118 | 122 | 5 | inferred_complete_timeline |
| `Action_CrackBlock` | 130 | 167 | 38 | inferred_complete_timeline |
| `Action_None` | 168 | 239 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 164 | 159 | inferred_complete_timeline |
| `Action_None` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 86 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–203 | 203 | 3 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–86 | 57 | 4 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 0–239 | 222 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–64 | 65 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–98 | 98 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 11–239 | 179 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 18–116 | 98 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 19–108 | 90 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 81–239 | 159 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 83–227 | 124 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 87–185 | 76 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 109–239 | 119 | 5 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 117–203 | 85 | 3 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 141–206 | 46 | 3 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 186–239 | 54 | 1 | Undefined position; Undefined team |
| `30` | `31` | Position_Unknown | Team_Unknown | 189–204 | 8 | 2 | Undefined position; Undefined team |
| `31` | `32` | Position_Unknown | Team_Unknown | 195–203 | 9 | 1 | Undefined position; Undefined team |
| `32` | `33` | Position_Unknown | Team_Unknown | 204–239 | 36 | 1 | Undefined position; Undefined team |
| `33` | `34` | Position_Unknown | Team_Unknown | 204–211 | 8 | 1 | Undefined position; Undefined team |
| `34` | `35` | Position_Unknown | Team_Unknown | 204–239 | 36 | 1 | Undefined position; Undefined team |
| `35` | `36` | Position_Unknown | Team_Unknown | 204–239 | 32 | 3 | Undefined position; Undefined team |
| `36` | `37` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `4` (5 segments found)
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Toss` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 82 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 60: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Row 60: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 60: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 60: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 60: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [6-164] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [9-44] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [50-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [86-116] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [118-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-102] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-156] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [79-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-52] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-30] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-70] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-40] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-72] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [6-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [37-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [6-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-80] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-44] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [9-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [36-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [11-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-112] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-203] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-148] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-170] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-203] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-211] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-213] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-239] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>
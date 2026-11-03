# Play-Annotation-Generator Annotation Review — OutRoutes_109

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_109`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 73
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `18` | `18` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `14` | 15 | START | 15 | 107 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `19` | 15 | START | 15 | 180 |
| ✅ EXACT | `Action_PassBlock` | C | `20` | `20` | 15 | START | 15 | 31 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 15 | START | 15 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `7` | `7` | 15 | START | 15 | 94 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `1` | `1` | 21 | START | 21 | 102 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `18` | 21 | END | 21 | 21 |
| ✅ EXACT | `Action_ThrowPass` | QB | `18` | `18` | 79 | START | 79 | 87 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `1` | `1` | 103 | START | 103 | 115 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `1` | 116 | START | 116 | 161 |

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
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_None` | 22 | 78 | 57 | inferred_complete_timeline |
| `Action_ThrowPass` | 79 | 87 | 9 | inferred_complete_timeline |
| `Action_None` | 88 | 180 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunOutRoute` | 21 | 102 | 82 | inferred_complete_timeline |
| `Action_SecureCatch` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 161 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 54 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 87 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 180 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 107 | 93 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 123 | 180 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 87 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 93 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 31 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 180 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 94 | 80 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 180 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 91 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 108 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 117 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 135 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 169 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 180 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 168 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 36–180 | 145 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 38–51 | 11 | 3 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 65–99 | 26 | 4 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 83–179 | 92 | 3 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 106–180 | 65 | 4 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 130–140 | 6 | 2 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 132–136 | 5 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 140–165 | 12 | 2 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 140–141 | 2 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 178–180 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 61 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-161] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-168] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-94] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-169] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-108] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-117] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-107] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [118-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [123-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-180] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-31] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-87] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-42] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-47] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-51] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-84] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-99] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-105] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-174] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-179] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-180] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-136] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-149] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '32' has 1 frames without a visible bounding box.
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
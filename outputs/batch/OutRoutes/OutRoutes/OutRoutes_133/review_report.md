# Play-Annotation-Generator Annotation Review — OutRoutes_133

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_133`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `20` | `20` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `20` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `11` | `11` | 16 | START | 16 | 86 |
| ✅ EXACT | `Action_PassBlock` | RT | `15` | `15` | 16 | START | 16 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 16 | START | 16 | 38 |
| ✅ EXACT | `Action_PassBlock` | LG | `21` | `21` | 16 | START | 16 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 16 | START | 16 | 61 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `20` | `20` | 21 | START | 21 | 91 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 21 | END | 21 | 21 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 60 | START | 60 | 70 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `20` | `20` | 92 | START | 92 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `20` | `20` | 103 | START | 103 | 119 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_SnapReceive` | 21 | 21 | 1 | inferred_complete_timeline |
| `Action_None` | 22 | 59 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 60 | 70 | 11 | inferred_complete_timeline |
| `Action_None` | 71 | 90 | 20 | inferred_complete_timeline |
| `Action_None` | 92 | 98 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

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
- **Visible Frames:** 0–106
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_RunOutRoute` | 21 | 91 | 71 | inferred_complete_timeline |
| `Action_SecureCatch` | 92 | 102 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 119 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 148 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 61 | 46 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 67 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 92 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 99 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 131 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 38 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 43 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 86 | 71 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 90 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 105 | 129 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 151 | 136 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 180 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 130 | 131 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 180 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 180 | 52 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–175 | 175 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 54–141 | 88 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 67–126 | 54 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 69–129 | 49 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 76–81 | 6 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 102–106 | 5 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 117–133 | 17 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 149–151 | 3 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 155–180 | 18 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 166–180 | 10 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 174–180 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 53 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-90] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-61] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-86] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-90] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [105-129] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-43] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-119] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [141-148] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-141] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-78] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-90] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-126] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-72] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-81] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-106] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-133] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-140] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-151] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-170] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-180] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-180] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
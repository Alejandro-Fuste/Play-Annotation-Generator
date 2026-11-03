# Play-Annotation-Generator Annotation Review — OutRoutes_127

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_127`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR1 | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | DT1 | defense | `14` | `14` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `12` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 15 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 16 | START | 16 | 148 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `18` | `18` | 16 | START | 16 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 16 | START | 16 | 48 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 16 | START | 16 | 42 |
| ✅ EXACT | `Action_PassBlock` | C | `21` | `21` | 16 | START | 16 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR1 | `6` | `6` | 16 | START | 16 | 48 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 16 | END | 16 | 16 |
| ✅ EXACT | `Action_ThrowPass` | DT1 | `14` | `14` | 81 | START | 81 | 91 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `6` | `6` | 112 | START | 112 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `6` | `6` | 121 | START | 121 | 172 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_SnapReceive` | 16 | 16 | 1 | inferred_complete_timeline |
| `Action_None` | 17 | 54 | 38 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_None` | 63 | 95 | 33 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 154 | 40 | inferred_complete_timeline |
| `Action_None` | 159 | 170 | 12 | inferred_complete_timeline |
| `Action_None` | 172 | 180 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 141 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 120 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 180 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_RunOutRoute` | 16 | 48 | 33 | inferred_complete_timeline |
| `Action_RunOutRoute` | 51 | 55 | 5 | inferred_complete_timeline |
| `Action_RunOutRoute` | 61 | 111 | 51 | inferred_complete_timeline |
| `Action_SecureCatch` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 172 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

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
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 148 | 133 | inferred_complete_timeline |
| `Action_PassBlock` | 157 | 173 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 48 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 117 | 52 | inferred_complete_timeline |
| `Action_PassBlock` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 133 | 172 | 40 | inferred_complete_timeline |
| `Action_PassBlock` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 66 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 42 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 53 | 105 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 120 | 162 | 43 | inferred_complete_timeline |
| `Action_PassBlock` | 164 | 180 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 57 | 42 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 133 | 62 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 180 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

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
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_ThrowPass` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_None` | 92 | 114 | 23 | inferred_complete_timeline |
| `Action_None` | 124 | 180 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 154 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 180 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 144 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 155 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 180 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 168 | 169 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 180 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 81–180 | 82 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 131–180 | 32 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 134–180 | 47 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 160–163 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (7 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 68 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-154] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [16-48] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [51-55] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [61-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [121-172] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-155] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-180] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-114] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-54] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-95] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-154] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-170] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-148] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [157-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [178-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-57] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-180] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [61-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [66-117] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [121-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [133-172] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [176-177] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [179-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-42] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [53-105] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [120-162] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [164-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-66] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-93] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-99] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-157] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>
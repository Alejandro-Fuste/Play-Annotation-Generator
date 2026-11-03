# Play-Annotation-Generator Annotation Review — OutRoutes_129

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_129`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 61
- **Validation Warnings:** 71
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
- **Inferred Coverage Segments (Action_None):** 35
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `3` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 69 |
| ✅ EXACT | `Action_PassBlock` | RT | `11` | `11` | 13 | START | 13 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 13 | START | 13 | 26 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 13 | START | 13 | 20 |
| ✅ EXACT | `Action_PassBlock` | LT | `20` | `20` | 13 | START | 13 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 13 | START | 13 | 14 |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | `1` | `1` | 18 | START | 18 | 90 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 18 | END | 18 | 18 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 53 | START | 53 | 63 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `1` | `1` | 91 | START | 91 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `1` | `1` | 100 | START | 100 | 129 |

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
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_SnapReceive` | 18 | 18 | 1 | inferred_complete_timeline |
| `Action_None` | 19 | 52 | 34 | inferred_complete_timeline |
| `Action_ThrowPass` | 53 | 63 | 11 | inferred_complete_timeline |
| `Action_None` | 64 | 172 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_RunOutRoute` | 18 | 90 | 73 | inferred_complete_timeline |
| `Action_SecureCatch` | 91 | 99 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 129 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 135 | 180 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

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
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 78 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 83 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 107 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 180 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 44 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 14 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 70 | 51 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 180 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 20 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 53 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 26 | 14 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 180 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 13 | 180 | 168 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–139
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 139 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 40 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 180 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 180 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

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
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 180 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
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
| `22` | `22` | Position_Unknown | Team_Unknown | 45–180 | 136 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 69–117 | 49 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 70–180 | 111 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 86–180 | 95 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 108–109 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 118–180 | 63 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 118–180 | 63 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 124–180 | 57 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 158–180 | 23 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 173–175 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 49 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [135-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-175] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-78] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-83] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-140] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-172] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-26] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-20] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-44] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [13-14] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-70] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-180] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-117] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-180] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-180] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '31' has 1 frames without a visible bounding box.
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
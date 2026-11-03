# Play-Annotation-Generator Annotation Review — OutRoutes_99

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_99`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR2 | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `18` | `18` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `5` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `14` | `14` | 12 | START | 12 | 17 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `15` | `15` | 12 | START | 12 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 12 | START | 12 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 12 | START | 12 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 12 | START | 12 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunOutRoute` | WR2 | `17` | `17` | 17 | START | 17 | 39 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 17 | END | 17 | 17 |
| ✅ EXACT | `Action_ThrowPass` | RB | `18` | `18` | 49 | START | 49 | 57 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `17` | `17` | 81 | START | 81 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `17` | `17` | 92 | START | 92 | 154 |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 17 | 1 | inferred_complete_timeline |
| `Action_None` | 18 | 239 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 48 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 49 | 57 | 9 | inferred_complete_timeline |
| `Action_None` | 58 | 173 | 116 | inferred_complete_timeline |
| `Action_None` | 175 | 239 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunOutRoute` | 17 | 39 | 23 | inferred_complete_timeline |
| `Action_RunOutRoute` | 41 | 80 | 40 | inferred_complete_timeline |
| `Action_SecureCatch` | 81 | 91 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 154 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 172 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–78
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 78 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 41 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 239 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 44 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 66 | 239 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 35 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 43 | 44 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 17 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 50 | 51 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 30 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 34 | 239 | 206 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 239 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 239 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 70 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 125 | 126 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 195 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 216 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 222 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 227 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 221 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 230 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 220 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 176 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 46–239 | 187 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 46–239 | 192 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 85–239 | 147 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 95–239 | 137 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 103–239 | 137 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 154–238 | 30 | 8 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 165–235 | 28 | 8 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 198–200 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 217–224 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunOutRoute` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 70 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-78] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-217] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-125] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-200] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-221] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-230] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [50-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-41] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [17-39] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-172] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-173] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-35] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [43-44] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-239] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-30] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-79] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-101] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-48] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-130] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-136] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-239] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-181] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-189] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-206] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-211] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-234] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-208] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-214] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-200] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-224] for track '31' has 1 frames without a visible bounding box.
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
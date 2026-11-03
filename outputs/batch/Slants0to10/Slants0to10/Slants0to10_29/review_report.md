# Play-Annotation-Generator Annotation Review — Slants0to10_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_29`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 70
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
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `20` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 2 | START | 2 | 6 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 2 | START | 2 | 7 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `19` | `19` | 2 | START | 2 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `21` | `21` | 2 | START | 2 | 6 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `5` | `5` | 2 | START | 2 | 98 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 7 | END | 7 | 7 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `0` | `0` | 10 | START | 10 | 53 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 63 | START | 63 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `0` | `0` | 110 | START | 110 | 165 |

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
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 7 | 1 | inferred_complete_timeline |
| `Action_None` | 8 | 62 | 55 | inferred_complete_timeline |
| `Action_ThrowPass` | 63 | 72 | 10 | inferred_complete_timeline |
| `Action_None` | 73 | 163 | 91 | inferred_complete_timeline |
| `Action_None` | 186 | 235 | 50 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 10 | 53 | 44 | inferred_complete_timeline |
| `Action_None` | 54 | 109 | 56 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 165 | 56 | inferred_complete_timeline |
| `Action_BallCarry` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 6 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 239 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 6 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 12 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 14 | 25 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 31 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 33 | 34 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 36 | 152 | 117 | inferred_complete_timeline |
| `Action_PassBlock` | 156 | 161 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 190 | 208 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 210 | 235 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 7 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 9 | 109 | 101 | inferred_complete_timeline |
| `Action_PassBlock` | 111 | 239 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 33 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 35 | 170 | 136 | inferred_complete_timeline |
| `Action_PassBlock` | 176 | 235 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 2 | 98 | 97 | inferred_complete_timeline |
| `Action_PassBlock` | 100 | 239 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 79 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 130 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

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
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 99 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 158 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 168 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 197 | 198 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 228 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 233 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 239 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 143 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 239 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 69–87 | 19 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 104–228 | 125 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 115–118 | 4 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 128–131 | 4 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 140–239 | 100 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 171–218 | 47 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 186–239 | 54 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 211–239 | 29 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (11 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 51 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [110-165] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-79] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-88] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-98] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [100-239] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-168] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-235] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-99] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-197] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-228] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-233] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-6] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [14-25] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-31] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [33-34] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [36-152] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [156-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [178-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [190-208] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [210-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-7] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-109] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [35-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [176-235] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [2-6] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [9-239] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-87] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-228] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-118] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-131] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-239] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-215] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-239] for track '29' has 3 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>
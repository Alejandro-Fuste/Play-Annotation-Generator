# Play-Annotation-Generator Annotation Review — Slants0to10_27

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_27`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 90
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 239 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `20` | 9 | END | 9 | 9 |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | `0` | `0` | 18 | START | 18 | 72 |
| ✅ EXACT | `Action_ThrowPass` | QB | `20` | `20` | 50 | START | 50 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `0` | `0` | 91 | START | 91 | 221 |

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
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_SnapReceive` | 9 | 9 | 1 | inferred_complete_timeline |
| `Action_None` | 10 | 49 | 40 | inferred_complete_timeline |
| `Action_ThrowPass` | 50 | 58 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 75 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 85 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 172 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 18 | 72 | 55 | inferred_complete_timeline |
| `Action_None` | 73 | 90 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 91 | 221 | 131 | inferred_complete_timeline |
| `Action_BallCarry` | 226 | 233 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–51
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 37 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 51 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 32 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 55 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 69 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 74 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 96 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 64 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 91 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 239 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 72 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 239 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 89 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 239 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 96 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 239 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 93 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 239 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 89 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 107 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 219 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 235 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 239 | 132 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 31–58 | 26 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 52–239 | 188 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 83–239 | 157 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 99–176 | 74 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 103–127 | 25 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 121–123 | 3 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 165–211 | 46 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 165–226 | 15 | 3 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 15, Column 'Pass Block': Could not parse frame number from '-' in entry '-,OL'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 65 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [91-221] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-233] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [237-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-91] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-96] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-219] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-75] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-89] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-93] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-89] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-72] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-85] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-172] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-91] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [50-58] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-32] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-55] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-74] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-81] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-96] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-51] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-58] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-127] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-123] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-189] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-211] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-171] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-182] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-182] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>
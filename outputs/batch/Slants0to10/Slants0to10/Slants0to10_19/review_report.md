# Play-Annotation-Generator Annotation Review — Slants0to10_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_19`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_PassBlock` | LT | `18` | `18` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `19` | 0 | START | 0 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 0 | START | 0 | 2 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 0 | START | 0 | 214 |
| ✅ EXACT | `Action_PassBlock` | RT | `4` | `4` | 0 | START | 0 | 239 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `11` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `19` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `21` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `4` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `9` | `Group` | 0 | START | 0 | 239 |
| ✅ EXACT | `Action_RunSlantRoute` | WR2 | `1` | `1` | 3 | START | 3 | 46 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 39 | START | 39 | 48 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `1` | 81 | START | 81 | 129 |

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
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_ThrowPass` | 39 | 48 | 10 | inferred_complete_timeline |
| `Action_None` | 49 | 239 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 172 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 184 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 187 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `9`</summary>

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
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 3 | 46 | 44 | inferred_complete_timeline |
| `Action_None` | 47 | 80 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 81 | 129 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–33
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PassBlock` | 0 | 33 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PassBlock` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 239 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PassBlock` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_PassBlock` | 218 | 239 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PassBlock` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PassBlock` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 140 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 228 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 150 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 172 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 235 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 131 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 164 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 234 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 219 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 235 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 128 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 89 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 198 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 235 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 173 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 129 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 148 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 168 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 176 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 239 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 239 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 42–47 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 62–69 | 5 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 101–239 | 139 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 107–176 | 70 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 115–118 | 4 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 118–119 | 2 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 122–125 | 4 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 125–180 | 6 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 153–156 | 4 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 155–157 | 3 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 181–185 | 5 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 183–224 | 41 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 194–239 | 46 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 61 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_BallCarry' range [81-129] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-222] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-219] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-235] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-110] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-148] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-168] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-176] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-235] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-184] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-131] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-164] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-234] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-128] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-173] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-140] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-228] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-89] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-198] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-212] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-235] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [0-33] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [0-2] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [0-214] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-47] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-69] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-118] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-125] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-126] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-156] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-157] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-185] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-219] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-224] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>
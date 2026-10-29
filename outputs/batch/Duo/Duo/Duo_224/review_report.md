# Play-Annotation-Generator Annotation Review — Duo_224

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_224`
- **Frame Range:** 0 to 274 (275 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 274
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 115
- **Validation Warnings:** 113
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 51
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `28` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `29` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | offense | `24` | `17` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RT | offense | `29` | `22` |
| ✅ EXACT | `Action_ComboBlock` | LB2 | defense | `6` | `6` |
| ✅ EXACT | `Action_ComboBlock` | CB2 | defense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 272 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 209 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `24` | `Group` | 0 | START | 77 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `25` | `Group` | 0 | START | 77 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `28` | `Group` | 0 | START | 80 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `29` | `Group` | 0 | START | 81 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 274 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | `24` | `17` | 124 | START | 124 | 128 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RT | `29` | `22` | 124 | START | N/A | N/A |
| ✅ EXACT | `Action_ComboBlock` | LB2 | `6` | `6` | 124 | START | 124 | 177 |
| ✅ EXACT | `Action_ComboBlock` | CB2 | `8` | `8` | 124 | START | 124 | 177 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 177 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 252 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 257 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 36 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 129 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 274 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 272 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 241 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 9 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 132 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 208 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 274 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `25`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 77–274
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 77 | 92 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 120 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 190 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 256 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 274 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `24`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 77–274
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 77 | 123 | 47 | inferred_complete_timeline |
| `Action_ComboBlock` | 124 | 128 | 5 | inferred_complete_timeline |
| `Action_ComboBlock` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 274 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `28`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `28`
- **team_side:** `offense`
- **Visible Frames:** 80–274
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 100 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 112 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 196 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 274 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `29`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `29`
- **team_side:** `offense`
- **Visible Frames:** 81–211
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 81 | 82 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 211 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 128 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 201 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 215 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 274 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 6–274
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 7 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 274 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `27`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `27`
- **team_side:** `defense`
- **Visible Frames:** 80–274
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 80 | 88 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 112 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 274 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ComboBlock` | 124 | 177 | 54 | inferred_complete_timeline |
| `Action_None` | 178 | 274 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_ComboBlock` | 124 | 177 | 54 | inferred_complete_timeline |
| `Action_None` | 178 | 262 | 85 | inferred_complete_timeline |
| `Action_None` | 265 | 274 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–5 | 4 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 80–274 | 96 | 6 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 193–196 | 4 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 239–274 | 36 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 250–274 | 25 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 266–267 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `17` (2 segments found)
- ❌ Missing segment for action `Action_ComboBlock` on target `22` (RT)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 100 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 274 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-252] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-262] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-73] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-128] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-201] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-215] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-100] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-241] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-132] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-208] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-129] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-140] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-274] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-82] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-123] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' for track '17' starts at frame 124, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ComboBlock' range [124-128] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [131-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-274] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-92] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-120] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-256] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-236] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-88] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-274] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-100] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-112] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-196] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-112] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-211] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-196] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-274] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.

</details>
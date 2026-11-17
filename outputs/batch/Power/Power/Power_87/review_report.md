# Play-Annotation-Generator Annotation Review — Power_87

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_87`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 151
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 10 | START | 10 | 188 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 10 | START | 10 | 318 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 10 | START | 10 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 10 | START | 10 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 10 | START | 10 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 10 | START | 10 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 10 | START | 10 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 10 | START | 10 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 10 | START | 10 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 10 | START | 10 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `21` | `21` | 141 | START | 141 | 146 |
| ✅ EXACT | `Action_PullBlock` | LG | `18` | `18` | 141 | START | 141 | 176 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 10–329
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 150 | 141 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 181 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 204 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 214 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 329 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 10–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 162 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 329 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 10–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 10–318
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 318 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 10–329
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 188 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 287 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 290 | 321 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 326 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 329 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 10–176
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 82 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 89 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 162 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 176 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 10–206
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 72 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 162 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 182 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 206 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 10–329
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 68 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 140 | 42 | inferred_complete_timeline |
| `Action_PullBlock` | 141 | 176 | 36 | inferred_complete_timeline |
| `Action_None` | 185 | 208 | 24 | inferred_complete_timeline |
| `Action_None` | 213 | 247 | 35 | inferred_complete_timeline |
| `Action_None` | 249 | 262 | 14 | inferred_complete_timeline |
| `Action_None` | 268 | 287 | 20 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_None` | 296 | 329 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 10–146
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 146 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 10–194
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 90 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 159 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 10–329
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 43 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 66 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 181 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 329 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 10–329
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 69 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 78 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 86 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 160 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 182 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 207 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 221 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 276 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 329 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 10–161
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 69 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 86 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 161 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 10–240
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 88 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 142 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 179 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 206 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 228 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 240 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 10–225
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 214 | 205 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 225 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 10–329
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 162 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 180 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 199 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 226 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 241 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 329 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 10–225
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 182 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 206 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 10–272
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 272 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 329 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 10–324
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 324 | 315 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 10–309 | 126 | 13 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 167–224 | 35 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 187–194 | 8 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 220–224 | 4 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 225–227 | 3 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 251–329 | 71 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 264–266 | 3 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 265–312 | 32 | 5 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 267–328 | 53 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 274–284 | 7 | 2 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 286–291 | 6 | 1 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 289–290 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 315–316 | 2 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 120 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [10-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-287] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-321] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-326] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-318] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-324] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-182] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-221] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-89] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-162] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-162] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-199] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-204] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-214] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-241] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-162] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-214] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-225] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-90] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-194] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-86] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-160] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-207] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-221] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-276] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-88] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-142] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-228] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-240] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-214] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-69] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-161] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [141-176] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-208] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-247] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-262] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-287] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-78] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-162] for track '19' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-206] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-43] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-66] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-181] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-45] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [141-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [166-170] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [173-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-199] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-283] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-309] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-206] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-194] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-255] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-261] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-266] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-277] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-288] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-328] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-278] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-291] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-290] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-303] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-329] for track '35' has 1 frames without a visible bounding box.
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

</details>
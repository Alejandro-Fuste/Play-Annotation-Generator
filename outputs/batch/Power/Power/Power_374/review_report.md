# Play-Annotation-Generator Annotation Review — Power_374

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_374`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `6` | `6` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 21 | START | 21 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 21 | START | 34 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 21 | START | 144 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 21 | START | 21 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 21 | START | 21 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 21 | START | 21 | 172 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 21 | START | 21 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 21 | START | 21 | 138 |
| ✅ EXACT | `Action_DownBlock` | RT | `6` | `6` | 139 | START | 139 | 187 |
| ✅ EXACT | `Action_DownBlock` | C | `8` | `8` | 139 | START | 139 | 169 |
| ✅ EXACT | `Action_PullBlock` | LG | `9` | `9` | 139 | START | 139 | 187 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 21–172
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 172 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 21–299
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 192 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 219 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 235 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 262 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 299 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 144–241
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 144 | 171 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 220 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 241 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 21–234
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 234 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 21–249
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 138 | 118 | inferred_complete_timeline |
| `Action_PullBlock` | 139 | 187 | 49 | inferred_complete_timeline |
| `Action_None` | 188 | 212 | 25 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 21–169
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 138 | 118 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 169 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 34–271
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 34 | 171 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 204 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 215 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 235 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 258 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 271 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 21–258
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 138 | 118 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 187 | 49 | inferred_complete_timeline |
| `Action_None` | 188 | 245 | 58 | inferred_complete_timeline |
| `Action_None` | 251 | 258 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 21–279
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 210 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 247 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 279 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 21–195
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 195 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 27–260
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 47 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 52 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 76 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 122 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 132 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 152 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 180 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 260 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 21–210
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 31 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 64 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 158 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 178 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 203 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 21–256
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 171 | 151 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 206 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 256 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 21–299
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 197 | 177 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 254 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 268 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 299 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 21–271
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 271 | 251 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `19` | Position_Unknown | Team_Unknown | 171–175 | 5 | 1 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 177–225 | 49 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 178–294 | 117 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 184–274 | 86 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 189–293 | 105 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 191–299 | 59 | 4 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 202–250 | 45 | 2 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 209–299 | 88 | 2 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 214–260 | 41 | 3 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 216–299 | 81 | 3 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 235–266 | 25 | 3 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 253–299 | 47 | 1 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 282–297 | 16 | 1 | Undefined position; Undefined team |
| `28` | `45` | Position_Unknown | Team_Unknown | 284–297 | 14 | 1 | Undefined position; Undefined team |
| `29` | `47` | Position_Unknown | Team_Unknown | 287–299 | 9 | 2 | Undefined position; Undefined team |
| `30` | `48` | Position_Unknown | Team_Unknown | 289–292 | 4 | 1 | Undefined position; Undefined team |
| `31` | `50` | Position_Unknown | Team_Unknown | 291–292 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 81 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [21-271] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-247] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-279] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-195] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-268] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-245] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-258] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-169] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-212] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-192] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-219] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-235] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-262] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-31] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-64] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-158] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-203] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-47] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-52] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-76] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-122] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-132] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-152] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-228] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-171] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-204] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-215] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-235] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-258] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-271] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-171] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-220] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-241] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-175] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-294] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-234] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-245] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-274] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-293] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-234] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-238] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-242] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-227] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-274] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-243] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-249] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-266] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-297] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-292] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-292] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-292] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>
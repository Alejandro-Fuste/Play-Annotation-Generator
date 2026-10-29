# Play-Annotation-Generator Annotation Review — Duo_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_60`
- **Frame Range:** 0 to 298 (299 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 298
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `19` | `19` |
| ✅ EXACT | `Action_ComboBlock` | SAF2 | defense | `20` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 12 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 12 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 12 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 12 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 12 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 2 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 12 | 70 |
| ✅ EXACT | `Action_ComboBlock` | LT | `11` | `11` | 162 | START | 162 | 174 |
| ✅ EXACT | `Action_ComboBlock` | RG | `17` | `17` | 162 | START | 162 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | Position_Unknown | `19` | `19` | 162 | START | 162 | 175 |
| ✅ EXACT | `Action_ComboBlock` | SAF2 | `20` | `20` | 162 | START | 162 | 201 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 201 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 12–259
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 67 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 72 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 84 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 89 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 259 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 12–287
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 238 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 248 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 252 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 259 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 265 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 272 | 287 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 12–288
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 70 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 213 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 216 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 288 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 12–174
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 57 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 161 | 99 | inferred_complete_timeline |
| `Action_ComboBlock` | 162 | 174 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 2–55
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 10 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 55 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 12–283
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 87 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 161 | 71 | inferred_complete_timeline |
| `Action_ComboBlock` | 162 | 201 | 40 | inferred_complete_timeline |
| `Action_None` | 202 | 202 | 1 | inferred_complete_timeline |
| `Action_None` | 204 | 283 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 12–104
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 99 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 104 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 12–179
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 51 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 179 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 12–268
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 110 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 113 | 231 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 268 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 13–248
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 63 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 154 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 239 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 248 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `22`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 13–257
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 149 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 257 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 12–174
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 174 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–298
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 259 | 184 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 298 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 12–298
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 42 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 298 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 12–298
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 239 | 228 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 276 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 279 | 298 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 12–298
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 19 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 125 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 161 | 35 | inferred_complete_timeline |
| `Action_ComboBlock` | 162 | 201 | 40 | inferred_complete_timeline |
| `Action_None` | 202 | 298 | 97 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–11 | 12 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–12 | 13 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–10 | 11 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–11 | 12 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–10 | 10 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 12–298 | 264 | 6 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 12–298 | 282 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 18–128 | 27 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 55–298 | 178 | 10 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 79–193 | 94 | 5 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 108–110 | 3 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 138–272 | 129 | 2 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 143–244 | 98 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 183–263 | 58 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 198–298 | 101 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 201–298 | 98 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 221–298 | 78 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 250–260 | 11 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 284–294 | 11 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 285–286 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 93 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-259] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-10] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-55] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-276] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-298] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-70] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-213] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-288] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-231] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-248] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-252] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-259] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-265] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-287] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [162-174] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-42] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-298] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-99] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-179] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-84] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-259] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-87] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [162-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 202, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [202-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-283] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-83] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-151] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-249] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-264] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [162-175] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [179-193] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-298] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-19] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-125] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-63] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [241-248] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-257] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-64] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-79] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-92] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-127] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-140] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-158] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-273] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-80] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-176] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-185] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-110] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-272] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-204] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-244] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-189] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-263] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-298] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-298] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-260] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-294] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-286] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
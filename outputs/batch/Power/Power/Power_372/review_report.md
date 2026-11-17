# Play-Annotation-Generator Annotation Review — Power_372

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_372`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 0
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 18 | START | 18 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 18 | START | 18 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `15` | `Group` | 18 | START | 24 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 18 | START | 26 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `18` | `Group` | 18 | START | 69 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 18 | START | 18 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 18 | START | 18 | 146 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 18 | START | 18 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 18 | START | 18 | 175 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `11` | `11` | 111 | START | 111 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `3` | `3` | 111 | START | 111 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `8` | `8` | 111 | START | 111 | 146 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 146 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 185 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 269 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `18`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 69–209
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 69 | 97 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 145 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 155 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 209 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 24–204
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 24 | 138 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 185 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 188 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 204 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 18–223
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 120 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 134 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 158 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 223 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 18–191
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 175 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 191 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 110 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 111 | 163 | 53 | inferred_complete_timeline |
| `Action_DownBlock` | 168 | 195 | 28 | inferred_complete_timeline |
| `Action_None` | 196 | 269 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 26–118
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 26 | 118 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 18–269
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 110 | 93 | inferred_complete_timeline |
| `Action_PullBlock` | 111 | 146 | 36 | inferred_complete_timeline |
| `Action_PullBlock` | 151 | 195 | 45 | inferred_complete_timeline |
| `Action_None` | 196 | 218 | 23 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 240 | 7 | inferred_complete_timeline |
| `Action_None` | 243 | 269 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 18–158
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 29 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 122 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 151 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 158 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–199
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 151 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 160 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 168 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 172 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 190 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 199 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 18–191
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 185 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 191 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 18–154
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 110 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 111 | 151 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 154 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 19–195
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 24 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 59 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 178 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 187 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 195 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 264 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 259 | 242 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 269 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 18–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 269 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 18–157
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 157 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `20` | Position_Unknown | Team_Unknown | 96–103 | 8 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 152–206 | 55 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 159–166 | 8 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 161–269 | 106 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 174–269 | 96 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 197–199 | 3 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 203–269 | 63 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 218–221 | 4 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 242–244 | 3 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 244–269 | 20 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 249–260 | 6 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 257–269 | 13 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 63 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [18-157] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-259] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-269] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [111-163] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-185] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-151] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-190] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-199] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-146] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-185] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [111-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-218] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-240] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-191] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-134] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-223] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [111-151] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-29] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-122] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-158] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-59] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-178] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-187] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-195] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-97] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-145] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-155] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-263] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-199] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-216] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-244] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-250] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-269] for track '26' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-252] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-269] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '31' has 1 frames without a visible bounding box.
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
# Play-Annotation-Generator Annotation Review — RPO_90

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_90`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `4` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_PullBall` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `19` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `11` | `11` | 64 | START | 64 | 84 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `13` | `13` | 64 | START | 64 | 123 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `16` | `16` | 64 | START | 64 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `18` | `18` | 64 | START | 64 | 116 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `20` | 64 | START | 64 | 64 |
| ✅ EXACT | `Action_ReadDefender` | QB | `17` | `17` | 71 | START | 71 | 81 |
| ✅ EXACT | `Action_PullBall` | QB | `17` | `17` | 82 | START | 82 | 98 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 115 | START | 115 | 123 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 70 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 71 | 81 | 11 | inferred_complete_timeline |
| `Action_PullBall` | 82 | 98 | 17 | inferred_complete_timeline |
| `Action_None` | 99 | 114 | 16 | inferred_complete_timeline |
| `Action_ThrowPass` | 115 | 123 | 9 | inferred_complete_timeline |
| `Action_None` | 124 | 269 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 219 | 157 | inferred_complete_timeline |
| `Action_None` | 222 | 223 | 2 | inferred_complete_timeline |
| `Action_None` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 269 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 228 | 166 | inferred_complete_timeline |
| `Action_None` | 230 | 246 | 17 | inferred_complete_timeline |
| `Action_None` | 250 | 265 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 269 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 191 | 129 | inferred_complete_timeline |
| `Action_None` | 193 | 234 | 42 | inferred_complete_timeline |
| `Action_None` | 257 | 262 | 6 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 84 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 113 | 22 | inferred_complete_timeline |
| `Action_None` | 125 | 252 | 128 | inferred_complete_timeline |
| `Action_None` | 255 | 265 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 123 | 60 | inferred_complete_timeline |
| `Action_None` | 124 | 143 | 20 | inferred_complete_timeline |
| `Action_None` | 151 | 157 | 7 | inferred_complete_timeline |
| `Action_None` | 164 | 269 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 68 | 70 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 74 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 85 | 123 | 39 | inferred_complete_timeline |
| `Action_None` | 124 | 144 | 21 | inferred_complete_timeline |
| `Action_None` | 147 | 204 | 58 | inferred_complete_timeline |
| `Action_None` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 116 | 53 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 132 | 269 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 63 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 64 | 123 | 60 | inferred_complete_timeline |
| `Action_None` | 124 | 227 | 104 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 255 | 21 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 229 | 167 | inferred_complete_timeline |
| `Action_None` | 231 | 237 | 7 | inferred_complete_timeline |
| `Action_None` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_None` | 249 | 269 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 108 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–260
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 199 | 137 | inferred_complete_timeline |
| `Action_None` | 201 | 234 | 34 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 257 | 260 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 112 | 50 | inferred_complete_timeline |
| `Action_None` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 133 | 6 | inferred_complete_timeline |
| `Action_None` | 135 | 255 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 226 | 164 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 262 | 24 | inferred_complete_timeline |
| `Action_None` | 267 | 269 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 269 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 222 | 160 | inferred_complete_timeline |
| `Action_None` | 229 | 235 | 7 | inferred_complete_timeline |
| `Action_None` | 237 | 238 | 2 | inferred_complete_timeline |
| `Action_None` | 245 | 250 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 238 | 176 | inferred_complete_timeline |
| `Action_None` | 240 | 242 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 269 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 189 | 127 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_None` | 63 | 245 | 183 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 84–85 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 109–111 | 3 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 115–126 | 6 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 155–182 | 10 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 162–179 | 13 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 187–212 | 8 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 200–229 | 30 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 223–224 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 227–269 | 21 | 4 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 237–238 | 2 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 246–261 | 9 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 252–269 | 18 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 75 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [63-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-226] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-262] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-229] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-269] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-228] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-265] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-191] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-234] for track '6' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-262] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-222] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-250] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-219] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-108] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-112] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-133] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-255] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-252] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-265] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-199] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-234] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-227] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-245] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-238] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-143] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-157] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [64-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '20' starts at frame 64, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [64-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [68-70] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-229] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-233] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '32' has 1 frames without a visible bounding box.
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

</details>
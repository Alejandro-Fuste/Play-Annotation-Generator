# Play-Annotation-Generator Annotation Review — RPO_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `RPO_49`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_RPO`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING
- **Non-Temporal Descriptors:** 1
  - **Non-Temporal Action Descriptor:** `Action_RunSlantRoute` | actor_track_id `7` | source `Route` | no temporal frame

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | RB | offense | `9` | `9` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `16` | 104 | START | 104 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `18` | 104 | START | 104 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 104 | START | 104 | 129 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 104 | START | 104 | 109 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 104 | START | 104 | 159 |
| ✅ EXACT | `Action_ReadDefender` | QB | `17` | `17` | 108 | START | 108 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBall` | RB | `9` | `9` | 121 | START | 121 | 123 |
| ✅ EXACT | `Action_ThrowPass` | RB | `9` | `9` | 146 | START | 146 | 159 |

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
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 108 | 160 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 120 | 18 | inferred_complete_timeline |
| `Action_PullBall` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_PullBall` | 130 | 133 | 4 | inferred_complete_timeline |
| `Action_None` | 134 | 145 | 12 | inferred_complete_timeline |
| `Action_ThrowPass` | 146 | 159 | 14 | inferred_complete_timeline |
| `Action_None` | 160 | 226 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 119 | 13 | inferred_complete_timeline |
| `Action_None` | 121 | 158 | 38 | inferred_complete_timeline |
| `Action_None` | 162 | 191 | 30 | inferred_complete_timeline |
| `Action_None` | 196 | 204 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 175 | 73 | inferred_complete_timeline |
| `Action_None` | 179 | 215 | 37 | inferred_complete_timeline |
| `Action_None` | 217 | 329 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–309
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 117 | 15 | inferred_complete_timeline |
| `Action_None` | 119 | 128 | 10 | inferred_complete_timeline |
| `Action_None` | 131 | 140 | 10 | inferred_complete_timeline |
| `Action_None` | 142 | 166 | 25 | inferred_complete_timeline |
| `Action_None` | 169 | 294 | 126 | inferred_complete_timeline |
| `Action_None` | 296 | 297 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 309 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 146 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 159 | 56 | inferred_complete_timeline |
| `Action_None` | 160 | 242 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 140 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 152 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_None` | 160 | 226 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 111 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 134 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 129 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 103 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 109 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 138 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 149 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 160 | 170 | 11 | inferred_complete_timeline |
| `Action_None` | 172 | 193 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 329 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–304
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 155 | 53 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 304 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 154 | 52 | inferred_complete_timeline |
| `Action_None` | 168 | 217 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 195 | 93 | inferred_complete_timeline |
| `Action_None` | 197 | 329 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 148 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 156 | 54 | inferred_complete_timeline |
| `Action_None` | 174 | 192 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 152 | 50 | inferred_complete_timeline |
| `Action_None` | 156 | 203 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 195 | 93 | inferred_complete_timeline |
| `Action_None` | 199 | 329 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 168 | 66 | inferred_complete_timeline |
| `Action_None` | 172 | 196 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 304 | 202 | inferred_complete_timeline |
| `Action_None` | 307 | 308 | 2 | inferred_complete_timeline |
| `Action_None` | 312 | 316 | 5 | inferred_complete_timeline |
| `Action_None` | 319 | 325 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_None` | 103 | 179 | 77 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 125–162 | 20 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 150–227 | 69 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 161–173 | 10 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 166–329 | 162 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 180–189 | 10 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 187–202 | 13 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 191–219 | 29 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 202–243 | 42 | 1 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 204–233 | 30 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 215–247 | 33 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 215–229 | 15 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 218–240 | 23 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 249–329 | 77 | 5 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 267–329 | 63 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 274–329 | 36 | 3 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 281–329 | 49 | 1 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 284–329 | 46 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 297–329 | 33 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBall` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 75 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [103-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-148] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-158] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-191] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-242] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-196] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-215] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-140] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-294] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-304] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-316] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-325] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBall' range [121-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-195] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-152] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-203] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-155] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-304] for track '13' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-140] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-152] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-226] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ReadDefender' range [108-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-111] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [156-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-129] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [104-109] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-149] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-170] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-193] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-166] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-227] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-213] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-219] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-243] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-233] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-229] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-240] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-302] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-309] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-329] for track '36' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>
# Play-Annotation-Generator Annotation Review — Duo_47

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_47`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `18` | `17` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 13 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 13 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `20` | `Group` | 0 | START | 13 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 13 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `23` | `Group` | 0 | START | 13 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 13 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 13 | 223 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 13 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `18` | `17` | 160 | START | 160 | 168 |
| ✅ EXACT | `Action_ComboBlock` | RG | `21` | `20` | 160 | START | 160 | 175 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 215 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 13–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 239 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 13–237
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 221 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 237 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 13–153
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 153 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 13–222
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 40 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 181 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 222 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 13–235
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 235 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 13–223
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 223 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 13–239
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 159 | 147 | inferred_complete_timeline |
| `Action_ComboBlock` | 160 | 175 | 16 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 13–239
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 31 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 159 | 126 | inferred_complete_timeline |
| `Action_ComboBlock` | 160 | 168 | 9 | inferred_complete_timeline |
| `Action_ComboBlock` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 175 | 215 | 41 | inferred_complete_timeline |
| `Action_None` | 216 | 239 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–239
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 164 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 207 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–239
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 191 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 203 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 13–237
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 168 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 197 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 232 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 13–159
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 159 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–171
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 82 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 105 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 171 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 13–239
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 169 | 157 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 203 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 239 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 13–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 63 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 106 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 239 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 11–12
- **Visible Samples:** 2

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 12 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 13–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 239 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 13–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 239 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 13–239
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 239 | 227 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–12 | 13 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–6 | 7 | 1 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 13–238 | 211 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 13–239 | 221 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 13–33 | 21 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 38–46 | 7 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 116–225 | 71 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 137–239 | 97 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 143–150 | 8 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 208–239 | 31 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 226–239 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '2' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-105] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-63] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-106] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-221] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-237] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-191] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-203] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-164] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-207] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-217] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-238] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-239] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-159] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-213] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-239] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-31] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-159] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [160-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [170-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [175-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-232] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-181] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [160-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-169] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-203] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-17] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-235] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-33] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-46] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-119] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-153] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-225] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-142] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-221] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-239] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-239] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>
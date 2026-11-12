# Play-Annotation-Generator Annotation Review — SplitZone_241

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_241`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 89
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE1 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 5 | START | 6 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 5 | START | 6 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 5 | START | 6 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 5 | START | 6 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 5 | START | 6 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 5 | START | 6 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 5 | START | 6 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 5 | START | 6 | 125 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 5 | START | 6 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 5 | START | 6 | 97 |
| ✅ EXACT | `Action_BallSnap` | DE1 | `11` | `11` | 98 | START | 98 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `15` | 101 | START | 101 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `18` | `18` | 101 | START | 101 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `20` | 101 | START | 101 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `21` | `21` | 101 | START | 101 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `4` | `4` | 105 | START | 105 | 147 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 109 | END | 98 | 109 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 118 | START | 118 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `6` | 126 | START | 126 | 162 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 185 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 6–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_SnapReceive` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 110 | 117 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 118 | 125 | 8 | inferred_complete_timeline |
| `Action_None` | 126 | 269 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 6–269
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 125 | 120 | inferred_complete_timeline |
| `Action_BallCarry` | 126 | 162 | 37 | inferred_complete_timeline |
| `Action_BallCarry` | 168 | 171 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 181 | 184 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 269 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 269 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 6–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 269 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–269
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 104 | 99 | inferred_complete_timeline |
| `Action_SplitBlock` | 105 | 147 | 43 | inferred_complete_timeline |
| `Action_SplitBlock` | 156 | 185 | 30 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 159 | 62 | inferred_complete_timeline |
| `Action_None` | 161 | 166 | 6 | inferred_complete_timeline |
| `Action_None` | 169 | 193 | 25 | inferred_complete_timeline |
| `Action_None` | 196 | 269 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 6–167
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 100 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 159 | 59 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 167 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 6–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 100 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 126 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 138 | 164 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 173 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 269 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 6–145
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 100 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 114 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 6–268
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 100 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 101 | 119 | 19 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 185 | 13 | inferred_complete_timeline |
| `Action_None` | 186 | 261 | 76 | inferred_complete_timeline |
| `Action_None` | 267 | 268 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 6–160
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_BallSnap` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 115 | 160 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 6–183
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 35 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 97 | 58 | inferred_complete_timeline |
| `Action_None` | 98 | 147 | 50 | inferred_complete_timeline |
| `Action_None` | 164 | 183 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–269
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 131 | 34 | inferred_complete_timeline |
| `Action_None` | 147 | 208 | 62 | inferred_complete_timeline |
| `Action_None` | 223 | 269 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 143 | 46 | inferred_complete_timeline |
| `Action_None` | 147 | 154 | 8 | inferred_complete_timeline |
| `Action_None` | 160 | 235 | 76 | inferred_complete_timeline |
| `Action_None` | 237 | 241 | 5 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–177
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 153 | 56 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_None` | 164 | 167 | 4 | inferred_complete_timeline |
| `Action_None` | 169 | 174 | 6 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 6–160
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 147 | 50 | inferred_complete_timeline |
| `Action_None` | 153 | 160 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–183
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 183 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 269 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–254
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 217 | 120 | inferred_complete_timeline |
| `Action_None` | 227 | 244 | 18 | inferred_complete_timeline |
| `Action_None` | 247 | 254 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 6–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 269 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–267
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 97 | 92 | inferred_complete_timeline |
| `Action_None` | 98 | 267 | 170 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 6–269 | 243 | 6 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 154–248 | 91 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 193–196 | 4 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 193–211 | 15 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 197–269 | 69 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 204–269 | 66 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 205–269 | 65 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 206–268 | 22 | 6 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 216–269 | 52 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 237–269 | 30 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 247–249 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (6 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 69 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 484: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [98-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-208] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-257] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-267] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [105-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [126-162] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [168-171] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-269] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-153] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-166] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-217] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-244] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [98-109] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-160] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-208] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-235] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-261] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-147] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-132] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [135-136] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [138-164] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-173] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-114] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [144-145] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [101-159] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [165-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-231] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-248] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-254] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-230] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-269] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
# Play-Annotation-Generator Annotation Review — BootPass_123

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_123`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 136
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `17` | `17` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | DT1 | defense | `6` | `6` |
| ✅ EXACT | `Action_FakeHandoff` | DT1 | defense | `6` | `6` |
| ✅ EXACT | `Action_BootAway` | DT1 | defense | `6` | `6` |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | DE1 | defense | `3` | `3` |
| ✅ EXACT | `Action_ThrowPass` | TE1 | offense | `20` | `20` |
| ✅ EXACT | `Action_SecureCatch` | DE2 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 22 | START | 22 | 47 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `14` | `14` | 40 | START | 48 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `17` | `17` | 40 | START | 40 | 42 |
| ✅ EXACT | `Action_RunBlock` | LT | `18` | `18` | 40 | START | 40 | 170 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `19` | `19` | 40 | START | 40 | 61 |
| ✅ EXACT | `Action_RunBlock` | LG | `9` | `9` | 40 | START | 40 | 129 |
| ✅ EXACT | `Action_SnapReceive` | DT1 | `6` | `6` | 47 | END | 22 | 47 |
| ✅ EXACT | `Action_FakeHandoff` | DT1 | `6` | `6` | 50 | START | 50 | 73 |
| ✅ EXACT | `Action_BootAway` | DT1 | `6` | `6` | 74 | START | 74 | 103 |
| ❌ MISSING SEGMENT | `Action_RunFlatRoute` | DE1 | `3` | `3` | 130 | START | N/A | N/A |
| ✅ EXACT | `Action_ThrowPass` | TE1 | `20` | `20` | 186 | START | 186 | 188 |
| ✅ EXACT | `Action_SecureCatch` | DE2 | `2` | `2` | 210 | START | 210 | 222 |

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
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 186 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 92 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 329 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 179 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_ThrowPass` | 186 | 188 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 329 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 170 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 129 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 22 | 47 | 26 | inferred_complete_timeline |
| `Action_RunBlock` | 48 | 261 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 53 | 201 | 149 | inferred_complete_timeline |
| `Action_RunBlock` | 206 | 224 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 230 | 242 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 250 | 251 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–75
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 61 | 22 | inferred_complete_timeline |
| `Action_RunBlock` | 73 | 75 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 122 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 76 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 83 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 113 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 209 | 82 | inferred_complete_timeline |
| `Action_SecureCatch` | 210 | 222 | 13 | inferred_complete_timeline |
| `Action_None` | 223 | 266 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 47 | 26 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_FakeHandoff` | 50 | 73 | 24 | inferred_complete_timeline |
| `Action_BootAway` | 74 | 103 | 30 | inferred_complete_timeline |
| `Action_None` | 104 | 271 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–270
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 170 | 149 | inferred_complete_timeline |
| `Action_None` | 176 | 207 | 32 | inferred_complete_timeline |
| `Action_None` | 212 | 270 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–277
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 277 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 112 | 91 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |
| `Action_None` | 125 | 126 | 2 | inferred_complete_timeline |
| `Action_None` | 129 | 145 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 329 | 308 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 122 | 101 | inferred_complete_timeline |
| `Action_None` | 138 | 173 | 36 | inferred_complete_timeline |
| `Action_None` | 175 | 179 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–278
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 278 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 203 | 182 | inferred_complete_timeline |
| `Action_None` | 205 | 268 | 64 | inferred_complete_timeline |
| `Action_None` | 271 | 300 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 190 | 169 | inferred_complete_timeline |
| `Action_None` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 200 | 5 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |
| `Action_None` | 208 | 215 | 8 | inferred_complete_timeline |
| `Action_None` | 221 | 225 | 5 | inferred_complete_timeline |
| `Action_None` | 232 | 236 | 5 | inferred_complete_timeline |
| `Action_None` | 238 | 329 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 51–244 | 179 | 8 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 74–107 | 21 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `25` | `25` | Position_Unknown | Team_Unknown | 110–239 | 130 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 132–134 | 3 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 136–250 | 88 | 6 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 171–253 | 59 | 8 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 183–242 | 60 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 188–274 | 77 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 197–329 | 133 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 206–244 | 37 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 217–236 | 20 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 222–247 | 24 | 2 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 247–260 | 14 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 261–315 | 55 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 261–329 | 69 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 276–283 | 7 | 2 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 291–296 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_RunBlock` for actor_track_id `14` (C): Annotated start 40 != Inferred start 48
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (2 segments found)
- ❌ Missing segment for action `Action_RunFlatRoute` on target `3` (DE1)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Segment 'Action_RunFlatRoute' for track '3' has invalid range: start=130, end=122. Clamping end to start.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [22–47], lower_priority='Action_RunBlock' annotated_start=40, effective_Action_RunBlock_start=48.
- ⚠️ Action 'Action_None' range [22-329] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-179] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-76] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-83] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-87] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-266] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-52] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-277] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-170] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-207] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-270] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-271] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [40-129] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-173] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-186] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-278] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [48-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-203] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-300] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-190] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-225] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [40-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [53-201] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [206-224] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [230-242] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [250-251] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [40-170] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [40-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [73-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [186-188] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-188] for track '22' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-201] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-224] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-244] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-107] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-239] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-195] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-200] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-242] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-274] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-212] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-244] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-236] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-225] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-247] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-260] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-315] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '41' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.

</details>
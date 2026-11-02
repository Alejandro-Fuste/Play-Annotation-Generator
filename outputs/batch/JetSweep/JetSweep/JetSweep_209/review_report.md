# Play-Annotation-Generator Annotation Review — JetSweep_209

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_209`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR2 | offense | `4` | `3` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_LeadBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 56 |
| ✅ EXACT | `Action_JetMotion` | WR2 | `4` | `3` | 20 | START | 20 | 81 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 57 | START | 57 | 71 |
| ✅ EXACT | `Action_LeadBlock` | Position_Unknown | `2` | `1` | 58 | START | 58 | 139 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `12` | 58 | START | 72 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `14` | `13` | 58 | START | 58 | 142 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `19` | 58 | START | 58 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `22` | `21` | 58 | START | 58 | 93 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `7` | 58 | START | 58 | 142 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 71 | END | 57 | 71 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 76 | START | 76 | 81 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `4` | `3` | 82 | START | 82 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 142 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_SnapReceive` | 57 | 71 | 15 | inferred_complete_timeline |
| `Action_None` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_Toss` | 76 | 81 | 6 | inferred_complete_timeline |
| `Action_None` | 82 | 176 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 234 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 240 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_JetMotion` | 20 | 81 | 62 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 329 | 248 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 241 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 142 | 85 | inferred_complete_timeline |
| `Action_None` | 143 | 296 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 142 | 85 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 57 | 71 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 72 | 75 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 83 | 142 | 60 | inferred_complete_timeline |
| `Action_None` | 143 | 252 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 93 | 36 | inferred_complete_timeline |
| `Action_ZoneBlock` | 102 | 142 | 41 | inferred_complete_timeline |
| `Action_None` | 143 | 218 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 142 | 85 | inferred_complete_timeline |
| `Action_None` | 143 | 194 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–279
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 279 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 214 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 113 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 87 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 176 | 120 | inferred_complete_timeline |
| `Action_None` | 186 | 238 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 244 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 329 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 329 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 220 | 164 | inferred_complete_timeline |
| `Action_None` | 222 | 226 | 5 | inferred_complete_timeline |
| `Action_None` | 228 | 238 | 11 | inferred_complete_timeline |
| `Action_None` | 240 | 241 | 2 | inferred_complete_timeline |
| `Action_None` | 243 | 244 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 186 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_None` | 57 | 61 | 5 | inferred_complete_timeline |
| `Action_None` | 63 | 329 | 267 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–241 | 233 | 5 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 97–98 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 104–113 | 6 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 109–212 | 98 | 5 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 138–161 | 23 | 2 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 138–198 | 44 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 157–161 | 5 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 190–191 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 195–208 | 14 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 204–222 | 18 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 216–226 | 11 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 239–241 | 3 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 257–264 | 8 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 267–277 | 11 | 1 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 273–329 | 57 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 287–289 | 3 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 297–298 | 2 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 302–329 | 28 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [57–71], lower_priority='Action_ZoneBlock' annotated_start=58, effective_Action_ZoneBlock_start=72.
- ⚠️ Action 'Action_None' range [57-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [58-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-186] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-279] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-296] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [72-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-252] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-220] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-238] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-176] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-238] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 57, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [57-61] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-244] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-194] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-93] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-218] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-154] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-171] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-155] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-198] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-208] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-218] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-222] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-226] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-264] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-277] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-289] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '37' has 1 frames without a visible bounding box.
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

</details>
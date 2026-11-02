# Play-Annotation-Generator Annotation Review — JetSweep_240

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_240`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 125
- **Validation Warnings:** 161
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | DE2 | defense | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_LeadBlock` | WR | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_Toss` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | DE2 | defense | `16` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `14` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 116 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | DE2 | `16` | `15` | 25 | START | 25 | 34 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 117 | START | 117 | 126 |
| ✅ EXACT | `Action_LeadBlock` | WR | `14` | `13` | 119 | START | 119 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `1` | `0` | 119 | START | 119 | 172 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `12` | 119 | START | 127 | 170 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `4` | 119 | START | 119 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `6` | 119 | START | 119 | 130 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `8` | 119 | START | 119 | 161 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 126 | END | 117 | 126 |
| ✅ EXACT | `Action_Toss` | QB | `4` | `3` | 137 | START | 137 | 148 |
| ✅ EXACT | `Action_BallCarry` | DE2 | `16` | `15` | 149 | START | 149 | 161 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 172 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_SnapReceive` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_None` | 127 | 136 | 10 | inferred_complete_timeline |
| `Action_Toss` | 137 | 148 | 12 | inferred_complete_timeline |
| `Action_None` | 149 | 178 | 30 | inferred_complete_timeline |
| `Action_None` | 212 | 213 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 168 | 52 | inferred_complete_timeline |
| `Action_None` | 177 | 213 | 37 | inferred_complete_timeline |
| `Action_None` | 217 | 223 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–127
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 118 | 55 | inferred_complete_timeline |
| `Action_LeadBlock` | 119 | 127 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 147 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 118 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 161 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 172 | 54 | inferred_complete_timeline |
| `Action_None` | 173 | 212 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 116 | 49 | inferred_complete_timeline |
| `Action_BallSnap` | 117 | 126 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 170 | 44 | inferred_complete_timeline |
| `Action_None` | 175 | 200 | 26 | inferred_complete_timeline |
| `Action_None` | 205 | 212 | 8 | inferred_complete_timeline |
| `Action_None` | 215 | 218 | 4 | inferred_complete_timeline |
| `Action_None` | 220 | 236 | 17 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |
| `Action_None` | 250 | 267 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 118 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 172 | 54 | inferred_complete_timeline |
| `Action_None` | 173 | 201 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 118 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 130 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 155 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 164 | 172 | 9 | inferred_complete_timeline |
| `Action_None` | 173 | 191 | 19 | inferred_complete_timeline |
| `Action_None` | 195 | 213 | 19 | inferred_complete_timeline |
| `Action_None` | 215 | 252 | 38 | inferred_complete_timeline |
| `Action_None` | 254 | 281 | 28 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 329 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 116 | 37 | inferred_complete_timeline |
| `Action_None` | 117 | 128 | 12 | inferred_complete_timeline |
| `Action_None` | 132 | 213 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_JetMotion` | 25 | 34 | 10 | inferred_complete_timeline |
| `Action_JetMotion` | 42 | 43 | 2 | inferred_complete_timeline |
| `Action_JetMotion` | 49 | 50 | 2 | inferred_complete_timeline |
| `Action_JetMotion` | 56 | 64 | 9 | inferred_complete_timeline |
| `Action_JetMotion` | 69 | 122 | 54 | inferred_complete_timeline |
| `Action_JetMotion` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_JetMotion` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_JetMotion` | 137 | 148 | 12 | inferred_complete_timeline |
| `Action_BallCarry` | 149 | 161 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 167 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 169 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 179 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 116 | 117 | inferred_complete_timeline |
| `Action_None` | 117 | 164 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 35–137 | 103 | 2 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 68–173 | 105 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 132–159 | 28 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 162–164 | 3 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 171–329 | 113 | 3 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 182–192 | 11 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 182–217 | 35 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 187–212 | 26 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 189–212 | 24 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 197–217 | 15 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 213–214 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 213–224 | 10 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 213–215 | 3 | 1 | Undefined position; Undefined team |
| `29` | `48` | Position_Unknown | Team_Unknown | 216–217 | 2 | 1 | Undefined position; Undefined team |
| `30` | `53` | Position_Unknown | Team_Unknown | 218–219 | 2 | 1 | Undefined position; Undefined team |
| `31` | `54` | Position_Unknown | Team_Unknown | 218–329 | 112 | 1 | Undefined position; Undefined team |
| `32` | `55` | Position_Unknown | Team_Unknown | 218–329 | 104 | 3 | Undefined position; Undefined team |
| `33` | `56` | Position_Unknown | Team_Unknown | 220–254 | 35 | 1 | Undefined position; Undefined team |
| `34` | `58` | Position_Unknown | Team_Unknown | 220–329 | 110 | 1 | Undefined position; Undefined team |
| `35` | `59` | Position_Unknown | Team_Unknown | 221–329 | 102 | 2 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 229–250 | 22 | 1 | Undefined position; Undefined team |
| `37` | `63` | Position_Unknown | Team_Unknown | 240–266 | 27 | 1 | Undefined position; Undefined team |
| `38` | `65` | Position_Unknown | Team_Unknown | 241–329 | 88 | 2 | Undefined position; Undefined team |
| `39` | `66` | Position_Unknown | Team_Unknown | 241–245 | 5 | 1 | Undefined position; Undefined team |
| `40` | `67` | Position_Unknown | Team_Unknown | 241–329 | 87 | 2 | Undefined position; Undefined team |
| `41` | `71` | Position_Unknown | Team_Unknown | 254–329 | 63 | 5 | Undefined position; Undefined team |
| `42` | `72` | Position_Unknown | Team_Unknown | 257–291 | 21 | 3 | Undefined position; Undefined team |
| `43` | `75` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `44` | `76` | Position_Unknown | Team_Unknown | 267–298 | 32 | 1 | Undefined position; Undefined team |
| `45` | `77` | Position_Unknown | Team_Unknown | 290–292 | 3 | 1 | Undefined position; Undefined team |
| `46` | `79` | Position_Unknown | Team_Unknown | 298–329 | 32 | 1 | Undefined position; Undefined team |
| `47` | `81` | Position_Unknown | Team_Unknown | 313–329 | 17 | 1 | Undefined position; Undefined team |
| `48` | `82` | Position_Unknown | Team_Unknown | 322–329 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `16` (8 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 119 != Inferred start 127
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [117–126], lower_priority='Action_ZoneBlock' annotated_start=119, effective_Action_ZoneBlock_start=127.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-213] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-223] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-147] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-212] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-179] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [119-130] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-155] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [160-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-191] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-252] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-281] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [119-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-213] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-170] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-200] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-212] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-267] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [119-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-116] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [25-34] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [42-43] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [49-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [56-64] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [69-122] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [127-128] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [131-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [149-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-159] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-197] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-267] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-212] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-220] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-270] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-308] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-254] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-311] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-250] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-266] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-279] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-304] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-297] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-304] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-329] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-286] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-298] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '45' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.

</details>
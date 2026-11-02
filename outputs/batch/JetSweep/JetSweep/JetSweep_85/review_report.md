# Play-Annotation-Generator Annotation Review — JetSweep_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_85`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 3
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `21` | `20` |
| ℹ️ GLOBAL EVENT | `Action_SealBlock` | N/A | N/A | N/A | N/A |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `10` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 122 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 116 | START | 116 | 131 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `21` | `20` | 120 | START | 120 | 145 |
| ℹ️ GLOBAL EVENT | `Action_SealBlock` | N/A | N/A | N/A | 123 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `14` | 123 | START | 132 | 179 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `17` | `16` | 123 | START | 123 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `2` | 123 | START | 123 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `6` | 123 | START | 123 | 179 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 123 | START | 123 | 146 |
| ✅ EXACT | `Action_LeadBlock` | RB | `10` | `9` | 125 | START | 125 | 179 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 131 | END | 116 | 131 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 137 | START | 137 | 145 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `21` | `20` | 146 | START | 146 | 269 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `8` | `7` | 147 | START | 147 | 179 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 179 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_SnapReceive` | 116 | 131 | 16 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |
| `Action_Toss` | 137 | 145 | 9 | inferred_complete_timeline |
| `Action_None` | 146 | 193 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_LeadBlock` | 125 | 179 | 55 | inferred_complete_timeline |
| `Action_None` | 180 | 256 | 77 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 184 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 269 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 179 | 57 | inferred_complete_timeline |
| `Action_None` | 180 | 189 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 167 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 180 | 187 | 8 | inferred_complete_timeline |
| `Action_None` | 189 | 193 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_BallSnap` | 116 | 131 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 179 | 48 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 190 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 179 | 57 | inferred_complete_timeline |
| `Action_None` | 180 | 199 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_ZoneBlock` | 123 | 146 | 24 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 147 | 179 | 33 | inferred_complete_timeline |
| `Action_None` | 180 | 203 | 24 | inferred_complete_timeline |
| `Action_None` | 206 | 269 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 152 | 37 | inferred_complete_timeline |
| `Action_None` | 158 | 159 | 2 | inferred_complete_timeline |
| `Action_None` | 161 | 169 | 9 | inferred_complete_timeline |
| `Action_None` | 172 | 269 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 162 | 47 | inferred_complete_timeline |
| `Action_None` | 181 | 269 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_None` | 142 | 162 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 133 | 18 | inferred_complete_timeline |
| `Action_None` | 138 | 269 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 153 | 38 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 269 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 201 | 86 | inferred_complete_timeline |
| `Action_None` | 203 | 269 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–26
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 204 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 151 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 117–180 | 64 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 120–269 | 150 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 140–161 | 5 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 187–191 | 5 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 188–269 | 79 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 202–269 | 68 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 218–269 | 52 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 229–269 | 38 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 235–237 | 3 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 260–261 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 123 != Inferred start 132
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [116–131], lower_priority='Action_ZoneBlock' annotated_start=123, effective_Action_ZoneBlock_start=132.
- ⚠️ Action 'Action_None' range [116-204] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-187] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-151] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-256] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-152] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-169] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-184] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-201] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [123-179] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-153] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-269] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-252] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '30' has 1 frames without a visible bounding box.
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

</details>
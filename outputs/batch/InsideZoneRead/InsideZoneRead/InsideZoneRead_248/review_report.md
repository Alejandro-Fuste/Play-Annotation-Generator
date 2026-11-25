# Play-Annotation-Generator Annotation Review — InsideZoneRead_248

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_248`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT2 | defense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `7` | `6` |
| ✅ EXACT | `Action_ReadDefender` | RB | offense | `7` | `6` |
| ✅ EXACT | `Action_Keep` | RB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 12 |
| ✅ EXACT | `Action_BallSnap` | DT2 | `10` | `9` | 10 | START | 10 | 27 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `11` | 13 | START | 13 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `3` | `2` | 13 | START | 13 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 13 | START | 13 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 13 | START | 13 | 91 |
| ✅ EXACT | `Action_ZoneBlock` | C | `9` | `8` | 13 | START | 13 | 91 |
| ✅ EXACT | `Action_SnapReceive` | RB | `7` | `6` | 27 | END | 10 | 27 |
| ✅ EXACT | `Action_ReadDefender` | RB | `7` | `6` | 31 | START | 31 | 36 |
| ✅ EXACT | `Action_Keep` | RB | `7` | `6` | 37 | START | 37 | 58 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 59 | START | 59 | 73 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 91 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 169 | 160 | inferred_complete_timeline |
| `Action_None` | 172 | 177 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 30 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_Keep` | 37 | 58 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 59 | 73 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 77 | 239 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 91 | 79 | inferred_complete_timeline |
| `Action_None` | 92 | 152 | 61 | inferred_complete_timeline |
| `Action_None` | 155 | 179 | 25 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 91 | 79 | inferred_complete_timeline |
| `Action_None` | 92 | 234 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 91 | 79 | inferred_complete_timeline |
| `Action_None` | 92 | 128 | 37 | inferred_complete_timeline |
| `Action_None` | 141 | 147 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 91 | 79 | inferred_complete_timeline |
| `Action_None` | 92 | 239 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 13 | 88 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 91 | 91 | 1 | inferred_complete_timeline |
| `Action_None` | 92 | 92 | 1 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 104 | 195 | 92 | inferred_complete_timeline |
| `Action_None` | 201 | 210 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 140 | 131 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 180 | 171 | inferred_complete_timeline |
| `Action_None` | 182 | 217 | 36 | inferred_complete_timeline |
| `Action_None` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 27 | 18 | inferred_complete_timeline |
| `Action_None` | 28 | 83 | 56 | inferred_complete_timeline |
| `Action_None` | 93 | 102 | 10 | inferred_complete_timeline |
| `Action_None` | 169 | 183 | 15 | inferred_complete_timeline |
| `Action_None` | 185 | 189 | 5 | inferred_complete_timeline |
| `Action_None` | 191 | 215 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 96 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 90 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 181 | 172 | inferred_complete_timeline |
| `Action_None` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 27–34 | 8 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 52–112 | 50 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 98–153 | 56 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 104–231 | 128 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 113–239 | 127 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 123–170 | 48 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 141–239 | 99 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 142–192 | 50 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 147–212 | 62 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 153–224 | 64 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 159–239 | 77 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 163–165 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 183–214 | 24 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 197–239 | 43 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 215–239 | 19 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 226–239 | 10 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 230–239 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 53 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [10-96] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-90] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [13-88] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 92, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [92-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-195] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-152] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-217] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [59-73] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-183] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-215] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-177] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-181] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-34] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-55] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-153] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-231] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-170] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-192] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-155] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-212] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-219] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-219] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-202] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-237] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_248'; source metadata written as null.

</details>
# Play-Annotation-Generator Annotation Review — JetSweep_192

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_192`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 62
- **Ball Tracks:** 0
- **Action Segments:** 176
- **Validation Warnings:** 240
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 153
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `1` | `0` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `22` | `19` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | SAF | defense | `2` | `1` |
| ✅ EXACT | `Action_Toss` | SAF | defense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `19` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `1` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 91 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 91 |
| ✅ EXACT | `Action_BallSnap` | C | `1` | `0` | 85 | START | 85 | 94 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `22` | `19` | 88 | START | 89 | 109 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `14` | `13` | 92 | START | 92 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `1` | `0` | 92 | START | 95 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `10` | `9` | 92 | START | 92 | 119 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `4` | `3` | 92 | START | 92 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `4` | 92 | START | 92 | 136 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `6` | `5` | 92 | START | 92 | 142 |
| ✅ EXACT | `Action_SnapReceive` | SAF | `2` | `1` | 94 | END | 85 | 94 |
| ✅ EXACT | `Action_Toss` | SAF | `2` | `1` | 105 | START | 105 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `22` | `19` | 110 | START | 110 | 113 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 142 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 128 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 110 | 26 | inferred_complete_timeline |
| `Action_None` | 112 | 113 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_LeadBlock` | 92 | 120 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 136 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 119 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 142 | 21 | inferred_complete_timeline |
| `Action_None` | 143 | 143 | 1 | inferred_complete_timeline |
| `Action_None` | 145 | 151 | 7 | inferred_complete_timeline |
| `Action_None` | 155 | 158 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_BallSnap` | 85 | 94 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 115 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 142 | 26 | inferred_complete_timeline |
| `Action_None` | 143 | 161 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 130 | 39 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 142 | 11 | inferred_complete_timeline |
| `Action_None` | 143 | 161 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_ZoneBlock` | 92 | 142 | 51 | inferred_complete_timeline |
| `Action_None` | 143 | 160 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 105 | 21 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 119 | 151 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 68 | 8 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 105 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 94 | 163 | 70 | inferred_complete_timeline |
| `Action_None` | 166 | 171 | 6 | inferred_complete_timeline |
| `Action_None` | 202 | 221 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 92 | 8 | inferred_complete_timeline |
| `Action_None` | 130 | 161 | 32 | inferred_complete_timeline |
| `Action_None` | 166 | 221 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 125 | 41 | inferred_complete_timeline |
| `Action_None` | 130 | 135 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_SnapReceive` | 85 | 94 | 10 | inferred_complete_timeline |
| `Action_None` | 95 | 104 | 10 | inferred_complete_timeline |
| `Action_Toss` | 105 | 109 | 5 | inferred_complete_timeline |
| `Action_None` | 110 | 161 | 52 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 151 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 101 | 17 | inferred_complete_timeline |
| `Action_None` | 103 | 108 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 11–389 | 287 | 6 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 56–269 | 190 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 88–389 | 276 | 11 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 89–389 | 279 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 97–132 | 33 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 116–132 | 17 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 127–161 | 31 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 134–336 | 202 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 140–161 | 22 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 146–147 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 162–167 | 6 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 169–389 | 178 | 6 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 173–338 | 162 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 174–284 | 97 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 178–218 | 30 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 179–197 | 19 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 191–346 | 155 | 2 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 212–345 | 127 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 214–285 | 72 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 216–389 | 130 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 216–389 | 148 | 10 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 216–287 | 61 | 4 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 223–288 | 63 | 3 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 226–309 | 84 | 1 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 226–389 | 84 | 5 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 227–291 | 56 | 2 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 237–304 | 68 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 239–301 | 62 | 2 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 240–268 | 16 | 3 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 242–298 | 30 | 4 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 243–276 | 29 | 2 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 249–315 | 32 | 6 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 293–312 | 20 | 1 | Undefined position; Undefined team |
| `51` | `71` | Position_Unknown | Team_Unknown | 294–316 | 23 | 1 | Undefined position; Undefined team |
| `52` | `72` | Position_Unknown | Team_Unknown | 295–314 | 20 | 1 | Undefined position; Undefined team |
| `53` | `73` | Position_Unknown | Team_Unknown | 296–307 | 9 | 2 | Undefined position; Undefined team |
| `54` | `74` | Position_Unknown | Team_Unknown | 302–303 | 2 | 1 | Undefined position; Undefined team |
| `55` | `80` | Position_Unknown | Team_Unknown | 325–381 | 54 | 2 | Undefined position; Undefined team |
| `56` | `81` | Position_Unknown | Team_Unknown | 325–337 | 13 | 1 | Undefined position; Undefined team |
| `57` | `86` | Position_Unknown | Team_Unknown | 342–389 | 48 | 1 | Undefined position; Undefined team |
| `58` | `88` | Position_Unknown | Team_Unknown | 343–389 | 46 | 2 | Undefined position; Undefined team |
| `59` | `89` | Position_Unknown | Team_Unknown | 345–389 | 45 | 1 | Undefined position; Undefined team |
| `60` | `90` | Position_Unknown | Team_Unknown | 356–389 | 34 | 1 | Undefined position; Undefined team |
| `61` | `92` | Position_Unknown | Team_Unknown | 374–389 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `22` (Position_Unknown): Annotated start 88 != Inferred start 89
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 46 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 46 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 92 |
| Missing visible bounding boxes during action | 145 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 386: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '0' (C): higher_priority='Action_BallSnap' [85–94], lower_priority='Action_ZoneBlock' annotated_start=92, effective_Action_ZoneBlock_start=95.
- ⚠️ Action 'Action_ZoneBlock' range [95-115] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-128] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-130] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-161] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-136] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-151] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-221] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [92-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-142] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '9' starts at frame 143, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [143-143] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-125] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [92-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-161] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-221] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-50] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-389] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-161] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-202] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-269] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-91] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-185] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-230] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-276] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-338] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-113] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [115-117] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [119-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-161] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-336] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-290] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-317] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-330] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-353] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-197] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-338] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-203] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-284] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-195] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-218] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-197] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-346] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-333] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-345] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-285] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-290] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-320] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-240] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-251] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-290] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-339] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-365] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-228] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-262] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-282] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-271] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-281] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-288] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-309] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-331] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-264] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-291] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-304] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-252] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-301] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-242] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-268] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-260] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-280] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-269] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-255] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-296] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-312] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-316] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-314] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-336] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-381] for track '55' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-337] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-355] for track '58' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.

</details>
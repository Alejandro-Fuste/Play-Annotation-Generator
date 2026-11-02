# Play-Annotation-Generator Annotation Review — JetSweep_167

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_167`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 131
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 93
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR2 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Toss` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 8 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 0 | START | 0 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR2 | `2` | `1` | 18 | START | 18 | 62 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 46 | START | 46 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_LeadBlock` | TE | `13` | `12` | 48 | START | 48 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 48 | START | 73 | 90 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 53 | END | 46 | 53 |
| ✅ EXACT | `Action_Toss` | QB | `12` | `11` | 64 | START | 64 | 69 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR2 | `2` | `1` | 70 | START | 70 | 141 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 149 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 53 | 8 | inferred_complete_timeline |
| `Action_None` | 54 | 63 | 10 | inferred_complete_timeline |
| `Action_Toss` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_None` | 70 | 178 | 109 | inferred_complete_timeline |
| `Action_None` | 181 | 196 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 131 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 239 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_JetMotion` | 18 | 62 | 45 | inferred_complete_timeline |
| `Action_JetMotion` | 64 | 69 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 70 | 141 | 72 | inferred_complete_timeline |
| `Action_BallCarry` | 148 | 191 | 44 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 238 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 221 | 176 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–208
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_LeadBlock` | 48 | 102 | 55 | inferred_complete_timeline |
| `Action_LeadBlock` | 112 | 146 | 35 | inferred_complete_timeline |
| `Action_None` | 152 | 159 | 8 | inferred_complete_timeline |
| `Action_None` | 162 | 208 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 8–217
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 9 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 17 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 35 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 45 | 9 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 50 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 90 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 94 | 149 | 56 | inferred_complete_timeline |
| `Action_None` | 150 | 159 | 10 | inferred_complete_timeline |
| `Action_None` | 171 | 174 | 4 | inferred_complete_timeline |
| `Action_None` | 190 | 217 | 28 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–54
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 54 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 239 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 195 | 150 | inferred_complete_timeline |
| `Action_None` | 197 | 239 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 138 | 93 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 163 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 146 | 101 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_None` | 188 | 222 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 162 | 117 | inferred_complete_timeline |
| `Action_None` | 165 | 239 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 123 | 78 | inferred_complete_timeline |
| `Action_None` | 126 | 168 | 43 | inferred_complete_timeline |
| `Action_None` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_None` | 184 | 206 | 23 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |
| `Action_None` | 216 | 239 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 14–239 | 180 | 11 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 55–239 | 140 | 6 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 61–158 | 94 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 65–224 | 150 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 73–239 | 156 | 4 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 74–221 | 148 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 74–152 | 79 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 74–188 | 112 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 79–159 | 81 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 105–132 | 18 | 2 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 143–163 | 21 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 148–177 | 20 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 156–166 | 11 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 168–174 | 6 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 170–226 | 57 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 179–236 | 57 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 185–239 | 53 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 188–237 | 48 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 189–239 | 51 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 195–229 | 28 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_LeadBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 83 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_LeadBlock' for track '12' (TE) duration 102 frames exceeds threshold 90 frames [start=48, end=149].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (C) duration 102 frames exceeds threshold 90 frames [start=48, end=149].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [46–53], lower_priority='Action_ZoneBlock' annotated_start=48, effective_Action_ZoneBlock_start=54.
- ⚠️ Action 'Action_None' range [46-221] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [18-62] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [70-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-191] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-138] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-163] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-162] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-206] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-222] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-131] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-178] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-196] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [48-102] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [112-146] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-208] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-9] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-17] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-35] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [46-50] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-90] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-217] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-35] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-78] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-122] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-192] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-225] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-92] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-80] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-224] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-173] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-221] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-163] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-166] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-166] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-226] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-201] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-204] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-237] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-229] for track '33' has 1 frames without a visible bounding box.
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

</details>
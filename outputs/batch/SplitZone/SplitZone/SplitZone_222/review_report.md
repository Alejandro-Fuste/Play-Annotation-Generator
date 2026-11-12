# Play-Annotation-Generator Annotation Review — SplitZone_222

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_222`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `1` | `Group` | 21 | START | 22 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 21 | START | 22 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 21 | START | 22 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 21 | START | 22 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 21 | START | 22 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 21 | START | 22 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 21 | START | 22 | 99 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 21 | START | 22 | 99 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 97 | START | 97 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `1` | `1` | 100 | START | 100 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 100 | START | 112 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `4` | `4` | 100 | START | 100 | 140 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `6` | 100 | START | 100 | 154 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 100 | START | 100 | 133 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `3` | 111 | END | 97 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `3` | `3` | 132 | START | 132 | 226 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 208 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 22–305
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 96 | 75 | inferred_complete_timeline |
| `Action_SnapReceive` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_None` | 112 | 131 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 132 | 226 | 95 | inferred_complete_timeline |
| `Action_BallCarry` | 231 | 277 | 47 | inferred_complete_timeline |
| `Action_BallCarry` | 280 | 305 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 22–151
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 96 | 75 | inferred_complete_timeline |
| `Action_None` | 97 | 142 | 46 | inferred_complete_timeline |
| `Action_None` | 145 | 151 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 22–164
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 31 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 96 | 64 | inferred_complete_timeline |
| `Action_None` | 97 | 149 | 53 | inferred_complete_timeline |
| `Action_None` | 154 | 164 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 22–265
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 99 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 154 | 55 | inferred_complete_timeline |
| `Action_ZoneBlock` | 208 | 208 | 1 | inferred_complete_timeline |
| `Action_None` | 209 | 225 | 17 | inferred_complete_timeline |
| `Action_None` | 227 | 265 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 22–141
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 99 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 133 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 141 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 22–297
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 96 | 75 | inferred_complete_timeline |
| `Action_BallSnap` | 97 | 111 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_None` | 220 | 267 | 48 | inferred_complete_timeline |
| `Action_None` | 273 | 280 | 8 | inferred_complete_timeline |
| `Action_None` | 291 | 297 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 22–140
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 99 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 140 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 22–133
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 99 | 78 | inferred_complete_timeline |
| `Action_ZoneBlock` | 100 | 133 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 22–294
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 96 | 75 | inferred_complete_timeline |
| `Action_None` | 97 | 156 | 60 | inferred_complete_timeline |
| `Action_None` | 233 | 244 | 12 | inferred_complete_timeline |
| `Action_None` | 246 | 250 | 5 | inferred_complete_timeline |
| `Action_None` | 257 | 259 | 3 | inferred_complete_timeline |
| `Action_None` | 261 | 265 | 5 | inferred_complete_timeline |
| `Action_None` | 285 | 294 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 22–137
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 96 | 75 | inferred_complete_timeline |
| `Action_None` | 97 | 123 | 27 | inferred_complete_timeline |
| `Action_None` | 132 | 137 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 61–71
- **Visible Samples:** 9

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 61 | 67 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 71 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 22–139
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 96 | 75 | inferred_complete_timeline |
| `Action_None` | 97 | 97 | 1 | inferred_complete_timeline |
| `Action_None` | 137 | 139 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 22–301
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 83 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 96 | 12 | inferred_complete_timeline |
| `Action_None` | 97 | 301 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 22–110
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 96 | 75 | inferred_complete_timeline |
| `Action_None` | 97 | 110 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 22–297
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 33 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 96 | 54 | inferred_complete_timeline |
| `Action_None` | 97 | 257 | 161 | inferred_complete_timeline |
| `Action_None` | 279 | 297 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 22–203
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 96 | 75 | inferred_complete_timeline |
| `Action_None` | 97 | 144 | 48 | inferred_complete_timeline |
| `Action_None` | 148 | 203 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 22–42 | 21 | 1 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 41–42 | 2 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 111–113 | 3 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 122–310 | 135 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 138–154 | 10 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 166–236 | 71 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 201–259 | 58 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 210–329 | 120 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 212–284 | 73 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 231–329 | 99 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 242–329 | 81 | 3 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 249–270 | 22 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 251–300 | 50 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 251–329 | 79 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 271–295 | 25 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 285–291 | 7 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 322–324 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 109 frames exceeds threshold 90 frames [start=100, end=208].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 109 frames exceeds threshold 90 frames [start=100, end=208].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [97–111], lower_priority='Action_ZoneBlock' annotated_start=100, effective_Action_ZoneBlock_start=112.
- ⚠️ Action 'Action_PreSnap' range [22-83] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-301] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-99] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [137-138] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-141] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-142] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [132-226] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-277] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [280-305] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-140] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-154] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 209, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [209-225] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [100-133] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-144] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '10' starts at frame 97, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [97-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-139] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-31] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-149] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-33] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-257] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-297] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-156] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-244] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-265] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-120] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [153-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-267] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-297] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-42] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-71] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-284] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-310] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-284] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-301] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-270] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-300] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-295] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>
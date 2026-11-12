# Play-Annotation-Generator Annotation Review — SplitZone_289

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_289`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 134
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 2
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ START CHANGED | `Action_PressEdge` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | Team_Unknown | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | defense | `15` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 2 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 36 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 37 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `12` | `12` | 93 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `12` | 93 | START | 93 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `14` | `13` | 93 | START | 93 | 126 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `3` | `3` | 93 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `4` | 93 | START | 93 | 99 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 93 | START | 93 | 154 |
| ⚠️ START CHANGED | `Action_PressEdge` | QB | `8` | `8` | 96 | START | 108 | 142 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | LG | `4` | `4` | 100 | START | 100 | 125 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 107 | END | 93 | 107 |
| ⚠️ START CHANGED | `Action_Handoff` | Position_Unknown | `21` | `20` | 115 | START | 128 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 132 | START | 132 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | `15` | `14` | 146 | START | 146 | 148 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_SnapReceive` | 93 | 107 | 15 | inferred_complete_timeline |
| `Action_PressEdge` | 108 | 142 | 35 | inferred_complete_timeline |
| `Action_None` | 143 | 178 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_BallCarry` | 132 | 180 | 49 | inferred_complete_timeline |
| `Action_BallCarry` | 183 | 185 | 3 | inferred_complete_timeline |
| `Action_BallCarry` | 187 | 359 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 36–222
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 92 | 57 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 126 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 154 | 24 | inferred_complete_timeline |
| `Action_None` | 155 | 222 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 92 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 99 | 7 | inferred_complete_timeline |
| `Action_SplitBlock` | 100 | 125 | 26 | inferred_complete_timeline |
| `Action_SplitBlock` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_None` | 155 | 209 | 55 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 2–256
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 4 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 61 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 80 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 93 | 1 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 117 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 145 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 154 | 7 | inferred_complete_timeline |
| `Action_None` | 155 | 172 | 18 | inferred_complete_timeline |
| `Action_None` | 179 | 224 | 46 | inferred_complete_timeline |
| `Action_None` | 252 | 256 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_ZoneBlock` | 93 | 154 | 62 | inferred_complete_timeline |
| `Action_None` | 155 | 359 | 205 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 143 | 51 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 215 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 41–219
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 41 | 111 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 129 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 145 | 1 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 146 | 148 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 150 | 187 | 38 | inferred_complete_timeline |
| `Action_None` | 188 | 219 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 92 | 21 | inferred_complete_timeline |
| `Action_None` | 93 | 102 | 10 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 111 | 113 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 130 | 16 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 137 | 141 | 5 | inferred_complete_timeline |
| `Action_None` | 143 | 164 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 173 | 81 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 138 | 46 | inferred_complete_timeline |
| `Action_None` | 142 | 145 | 4 | inferred_complete_timeline |
| `Action_None` | 150 | 207 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 144 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_None` | 93 | 245 | 153 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 53–226 | 174 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 79–359 | 274 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 109–128 | 16 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 119–120 | 2 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 126–222 | 97 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 128–171 | 41 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 155–183 | 29 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 168–293 | 122 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 174–359 | 179 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 186–359 | 174 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 190–345 | 156 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 202–226 | 22 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 214–359 | 143 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 216–327 | 102 | 4 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 230–232 | 3 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 232–359 | 128 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 233–359 | 126 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 235–241 | 7 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 255–359 | 105 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 263–278 | 14 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 269–359 | 76 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 334–359 | 26 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 352–356 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `12` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `3` (RG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ `Action_PressEdge` for actor_track_id `8` (QB): Annotated start 96 != Inferred start 108
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `4` (2 segments found)
- ⚠️ `Action_Handoff` for actor_track_id `21` (Position_Unknown): Annotated start 115 != Inferred start 128
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 80 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '3' has invalid range: start=93, end=73. Clamping end to start.
- ⚠️ Overlapping action conflict at frame 93 for track '12': 'Action_BallSnap' vs 'Action_ZoneBlock'. Overriding with 'Action_ZoneBlock'.
- ⚠️ Segment 'Action_Handoff' for track '20' has invalid range: start=128, end=127. Clamping end to start.
- ⚠️ Action 'Action_None' range [93-144] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-143] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-215] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-245] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [100-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-209] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [132-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [183-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-173] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-359] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-178] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-141] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-138] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-207] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-4] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-80] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-92] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' for track '12' starts at frame 93, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_ZoneBlock' range [93-93] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-172] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-224] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-256] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [93-126] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-222] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-111] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [146-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-226] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-128] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-183] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-268] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-293] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-273] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-345] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-217] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-328] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-220] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-311] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-319] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-232] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-338] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-241] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-272] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-284] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-356] for track '39' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.

</details>
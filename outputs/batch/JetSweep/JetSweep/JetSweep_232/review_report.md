# Play-Annotation-Generator Annotation Review — JetSweep_232

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_232`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 133
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 109 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 109 | START | 109 | 120 |
| ✅ EXACT | `Action_LeadBlock` | TE | `3` | `2` | 110 | START | 110 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `13` | `12` | 110 | START | 110 | 143 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `16` | 110 | START | 121 | 127 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `1` | 110 | START | 110 | 171 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `4` | `3` | 110 | START | 110 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `7` | 110 | START | 110 | 136 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 120 | END | 109 | 120 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 132 | START | 132 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `17` | 134 | START | 134 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | Position_Unknown | `18` | `17` | 160 | START | 160 | 208 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 189 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_SnapReceive` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_None` | 121 | 131 | 11 | inferred_complete_timeline |
| `Action_Toss` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 174 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 197 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_LeadBlock` | 110 | 189 | 80 | inferred_complete_timeline |
| `Action_None` | 190 | 299 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 143 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 180 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 171 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_BallSnap` | 109 | 120 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 121 | 127 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 140 | 160 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 136 | 27 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 170 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 179 | 180 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_ZoneBlock` | 110 | 189 | 80 | inferred_complete_timeline |
| `Action_None` | 190 | 231 | 42 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 235 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 119 | 11 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_None` | 132 | 231 | 100 | inferred_complete_timeline |
| `Action_None` | 235 | 249 | 15 | inferred_complete_timeline |
| `Action_None` | 256 | 299 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 116 | 8 | inferred_complete_timeline |
| `Action_None` | 121 | 162 | 42 | inferred_complete_timeline |
| `Action_None` | 167 | 171 | 5 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 299 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 127 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 149 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 250 | 142 | inferred_complete_timeline |
| `Action_None` | 270 | 271 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 169 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 130 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 108 | 109 | inferred_complete_timeline |
| `Action_None` | 109 | 242 | 134 | inferred_complete_timeline |
| `Action_None` | 245 | 249 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 108–218 | 104 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 137–299 | 149 | 5 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 139–167 | 29 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 148–299 | 152 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 157–212 | 56 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 166–178 | 13 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 195–299 | 98 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 197–264 | 68 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 203–299 | 53 | 5 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 211–265 | 48 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 215–299 | 78 | 3 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 215–299 | 85 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 220–299 | 80 | 1 | Undefined position; Undefined team |
| `32` | `34` | Position_Unknown | Team_Unknown | 226–273 | 47 | 2 | Undefined position; Undefined team |
| `33` | `35` | Position_Unknown | Team_Unknown | 227–299 | 54 | 4 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 244–299 | 54 | 2 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 250–299 | 43 | 5 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 260–299 | 34 | 2 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 261–299 | 39 | 1 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 261–263 | 3 | 1 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 262–299 | 38 | 1 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 273–299 | 27 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 278–299 | 22 | 1 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 283–299 | 15 | 2 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 292–298 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_JetMotion` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 27 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 27 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 54 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [109–120], lower_priority='Action_ZoneBlock' annotated_start=110, effective_Action_ZoneBlock_start=121.
- ⚠️ Action 'Action_None' range [109-169] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-171] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-231] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-250] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-197] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-162] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [172-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [175-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [179-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-242] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-149] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-108] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-235] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [110-143] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-249] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-127] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [121-127] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [132-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [140-160] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [134-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [160-208] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [213-218] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-250] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-291] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-167] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-212] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-178] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-202] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-264] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-219] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-231] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-249] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-265] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-266] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-299] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-245] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-273] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-269] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-295] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-261] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-299] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-266] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-299] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-299] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-299] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-298] for track '43' has 3 frames without a visible bounding box.
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

</details>
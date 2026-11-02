# Play-Annotation-Generator Annotation Review — JetSweep_153

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_153`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 55
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | WR1 | offense | `2` | `1` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `17` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | WR1 | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_JetMotion` | WR1 | `2` | `1` | 24 | START | 24 | 74 |
| ✅ EXACT | `Action_BallSnap` | LG | `17` | `16` | 48 | START | 48 | 49 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `11` | `10` | 50 | START | 50 | 111 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `16` | 50 | START | 50 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `20` | `19` | 50 | START | 50 | 55 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `21` | `20` | 50 | START | 50 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `7` | `6` | 50 | START | 50 | 67 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 61 | END | 48 | 61 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 66 | START | 66 | 74 |
| ✅ EXACT | `Action_BallCarry` | WR1 | `2` | `1` | 75 | START | 75 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 111 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_SnapReceive` | 48 | 61 | 14 | inferred_complete_timeline |
| `Action_None` | 62 | 65 | 4 | inferred_complete_timeline |
| `Action_Toss` | 66 | 74 | 9 | inferred_complete_timeline |
| `Action_None` | 75 | 161 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 147 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_JetMotion` | 24 | 74 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 75 | 299 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 173 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 186 | 139 | inferred_complete_timeline |
| `Action_None` | 188 | 201 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 111 | 62 | inferred_complete_timeline |
| `Action_None` | 112 | 174 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_BallSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 111 | 62 | inferred_complete_timeline |
| `Action_None` | 112 | 167 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 67 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 102 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 111 | 52 | inferred_complete_timeline |
| `Action_None` | 112 | 185 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 111 | 62 | inferred_complete_timeline |
| `Action_None` | 112 | 158 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 84 | 37 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 193 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 75 | 28 | inferred_complete_timeline |
| `Action_None` | 80 | 190 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 288 | 241 | inferred_complete_timeline |
| `Action_None` | 290 | 293 | 4 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 237 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 189 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 139 | 92 | inferred_complete_timeline |
| `Action_None` | 143 | 170 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 119 | 72 | inferred_complete_timeline |
| `Action_None` | 123 | 127 | 5 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 133 | 199 | 67 | inferred_complete_timeline |
| `Action_None` | 201 | 267 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 299 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 182 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_None` | 48 | 185 | 138 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–181 | 178 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 91–163 | 54 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 94–233 | 140 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 217–285 | 69 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 293–297 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 5 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 5 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 10 |
| Missing visible bounding boxes during action | 44 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [48-173] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-139] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-170] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-199] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-267] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-67] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [74-76] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [80-102] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [105-107] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-161] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-182] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-158] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-237] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-288] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-293] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-190] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-167] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-84] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-193] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-55] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-185] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-81] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-163] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-285] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '25' has 1 frames without a visible bounding box.
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

</details>
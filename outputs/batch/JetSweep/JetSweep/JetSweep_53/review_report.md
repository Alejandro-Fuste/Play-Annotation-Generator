# Play-Annotation-Generator Annotation Review — JetSweep_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_53`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 71
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | Team_Unknown | `26` | `21` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_LeadBlock` | TE2 | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | Team_Unknown | `31` | `24` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SealBlock` | Position_Unknown | Team_Unknown | `34` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `12` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `7` | `Group` | 0 | START | 0 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 119 |
| ⚠️ START CHANGED | `Action_JetMotion` | Position_Unknown | `26` | `21` | 17 | START | 117 | 290 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 116 | START | 116 | 129 |
| ✅ EXACT | `Action_LeadBlock` | TE2 | `7` | `6` | 120 | START | 120 | 157 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `10` | `9` | 120 | START | 120 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `13` | 120 | START | 130 | 166 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `19` | 120 | START | 120 | 175 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `4` | 120 | START | 120 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `8` | 120 | START | 120 | 175 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 129 | END | 116 | 129 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 136 | START | 136 | 147 |
| ⚠️ START CHANGED | `Action_BallCarry` | Position_Unknown | `31` | `24` | 148 | START | 171 | 183 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 175 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SealBlock` | Position_Unknown | `34` | `26` | 186 | START | 186 | 228 |

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
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_SnapReceive` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_None` | 130 | 135 | 6 | inferred_complete_timeline |
| `Action_Toss` | 136 | 147 | 12 | inferred_complete_timeline |
| `Action_None` | 148 | 221 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–186
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 186 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 131 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 160 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_LeadBlock` | 120 | 157 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 166 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–184
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 175 | 56 | inferred_complete_timeline |
| `Action_None` | 176 | 184 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_BallSnap` | 116 | 129 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 130 | 166 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 173 | 54 | inferred_complete_timeline |
| `Action_None` | 185 | 187 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 120 | 175 | 56 | inferred_complete_timeline |
| `Action_None` | 176 | 190 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 156 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 299 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 193 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 178 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 156 | 41 | inferred_complete_timeline |
| `Action_None` | 160 | 299 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 145 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 115 | 7 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_None` | 122 | 138 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 299 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_None` | 116 | 142 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–184 | 185 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 99–122 | 24 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 117–290 | 174 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 121–299 | 176 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 132–133 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 171–183 | 13 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 171–198 | 28 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 175–228 | 54 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 181–299 | 119 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 184–276 | 89 | 3 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 187–298 | 109 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 237–299 | 63 | 1 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 256–261 | 6 | 1 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 278–299 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_JetMotion` for actor_track_id `26` (Position_Unknown): Annotated start 17 != Inferred start 117
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `31` (Position_Unknown): Annotated start 148 != Inferred start 171

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [116–129], lower_priority='Action_ZoneBlock' annotated_start=120, effective_Action_ZoneBlock_start=130.
- ⚠️ Action 'Action_None' range [116-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [120-157] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-156] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [120-173] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-145] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-221] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [130-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [168-169] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-156] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-193] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-115] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-122] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [117-290] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [171-183] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SealBlock' range [186-228] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-276] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-292] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-261] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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
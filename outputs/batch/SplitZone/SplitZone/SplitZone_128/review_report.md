# Play-Annotation-Generator Annotation Review — SplitZone_128

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_128`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `20` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `3` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `16` | `Group` | 0 | START | 76 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `20` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 91 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `5` | `5` | 83 | START | 83 | 104 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `13` | `13` | 86 | START | 86 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `14` | 86 | START | 86 | 104 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `15` | `15` | 86 | START | 86 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `18` | `17` | 86 | START | 87 | 182 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `20` | `18` | 86 | START | 91 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `9` | `9` | 92 | START | 92 | 152 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `3` | 104 | END | 83 | 104 |
| ✅ EXACT | `Action_Handoff` | QB | `3` | `3` | 107 | START | 107 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 116 | START | 116 | 130 |
| ✅ EXACT | `Action_BlockSecondLevel` | Position_Unknown | `10` | `10` | 120 | START | 120 | 193 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 194 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_SnapReceive` | 83 | 104 | 22 | inferred_complete_timeline |
| `Action_None` | 105 | 106 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_None` | 116 | 123 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 130 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 174 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 178 | 265 | 88 | inferred_complete_timeline |
| `Action_BallCarry` | 268 | 270 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 76–120
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_None` | 83 | 87 | 5 | inferred_complete_timeline |
| `Action_None` | 89 | 97 | 9 | inferred_complete_timeline |
| `Action_None` | 99 | 106 | 8 | inferred_complete_timeline |
| `Action_None` | 113 | 120 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 91 | 92 | inferred_complete_timeline |
| `Action_SplitBlock` | 92 | 152 | 61 | inferred_complete_timeline |
| `Action_SplitBlock` | 156 | 194 | 39 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 104 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 91–299
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 91 | 93 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 95 | 160 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 165 | 194 | 30 | inferred_complete_timeline |
| `Action_None` | 195 | 299 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 87–249
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_ZoneBlock` | 87 | 182 | 96 | inferred_complete_timeline |
| `Action_ZoneBlock` | 192 | 194 | 3 | inferred_complete_timeline |
| `Action_None` | 195 | 249 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 100 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–257
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_ZoneBlock` | 86 | 95 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 127 | 132 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 182 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 187 | 194 | 8 | inferred_complete_timeline |
| `Action_None` | 195 | 257 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 175 | 93 | inferred_complete_timeline |
| `Action_None` | 187 | 223 | 37 | inferred_complete_timeline |
| `Action_None` | 230 | 299 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 114 | 32 | inferred_complete_timeline |
| `Action_None` | 116 | 299 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_BallSnap` | 83 | 104 | 22 | inferred_complete_timeline |
| `Action_None` | 105 | 133 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 173 | 91 | inferred_complete_timeline |
| `Action_None` | 182 | 203 | 22 | inferred_complete_timeline |
| `Action_None` | 214 | 229 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 231 | 149 | inferred_complete_timeline |
| `Action_None` | 235 | 299 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 111 | 29 | inferred_complete_timeline |
| `Action_None` | 171 | 173 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 136 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 183 | 101 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_None` | 198 | 219 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_None` | 83 | 155 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–228 | 216 | 5 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 96–187 | 92 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 110–133 | 12 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 110–267 | 152 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 110–128 | 7 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 134–174 | 41 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 134–166 | 33 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 137–144 | 8 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 139–299 | 160 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 146–192 | 41 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 146–156 | 11 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 149–299 | 141 | 5 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 151–153 | 3 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 162–299 | 138 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 168–169 | 2 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 170–299 | 128 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 182–253 | 70 | 3 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 220–299 | 78 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 224–297 | 70 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 241–299 | 59 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 242–253 | 11 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 264–299 | 36 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RT) duration 109 frames exceeds threshold 90 frames [start=86, end=194].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (C) duration 108 frames exceeds threshold 90 frames [start=87, end=194].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 104 frames exceeds threshold 90 frames [start=91, end=194].
- ⚠️ Action 'Action_None' range [83-136] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-111] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-231] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-133] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-183] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-219] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-203] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-229] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [92-152] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [120-193] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-228] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-130] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [141-174] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [178-265] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [268-270] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-223] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-100] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-104] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [86-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [117-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [127-132] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-257] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-249] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [91-93] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [95-160] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-155] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-174] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-166] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-281] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-155] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-192] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-162] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-240] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-201] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-235] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-256] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-271] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-297] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-248] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-253] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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
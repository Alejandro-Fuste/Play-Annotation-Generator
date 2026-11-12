# Play-Annotation-Generator Annotation Review — SplitZone_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_62`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 9
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `0` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 7 | START | 8 | 52 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 7 | START | 8 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 7 | START | 8 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 7 | START | 8 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 7 | START | 8 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 7 | START | 8 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 7 | START | 8 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 7 | START | 8 | 46 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `13` | 47 | START | 47 | 59 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 50 | START | 50 | 60 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `13` | `13` | 50 | START | 60 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `2` | 50 | START | 50 | 118 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `6` | 50 | START | 50 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `7` | 50 | START | 50 | 110 |
| ✅ EXACT | `Action_SplitBlock` | TE | `0` | `0` | 53 | START | 53 | 118 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 59 | END | 47 | 59 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `10` | `10` | 61 | START | 61 | 118 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 65 | START | 65 | 77 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `3` | 78 | START | 78 | 359 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 118 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 8–139
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 59 | 13 | inferred_complete_timeline |
| `Action_None` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 65 | 77 | 13 | inferred_complete_timeline |
| `Action_None` | 78 | 139 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 8–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 77 | 70 | inferred_complete_timeline |
| `Action_BallCarry` | 78 | 359 | 282 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 8–153
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 52 | 45 | inferred_complete_timeline |
| `Action_SplitBlock` | 53 | 118 | 66 | inferred_complete_timeline |
| `Action_None` | 119 | 153 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 8–258
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 49 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 118 | 69 | inferred_complete_timeline |
| `Action_None` | 119 | 187 | 69 | inferred_complete_timeline |
| `Action_None` | 254 | 258 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 8–175
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 49 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 118 | 69 | inferred_complete_timeline |
| `Action_None` | 119 | 175 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 8–150
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_BallSnap` | 47 | 59 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 60 | 118 | 59 | inferred_complete_timeline |
| `Action_None` | 119 | 150 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 8–129
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 49 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 110 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 119 | 1 | inferred_complete_timeline |
| `Action_None` | 122 | 129 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 8–169
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 49 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 60 | 11 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 61 | 118 | 58 | inferred_complete_timeline |
| `Action_None` | 119 | 169 | 51 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 8–282
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 47 | 282 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 8–115
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 47 | 115 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 8–247
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 47 | 247 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 8–123
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 47 | 92 | 46 | inferred_complete_timeline |
| `Action_None` | 122 | 123 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 8–132
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 47 | 132 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 8–93
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 47 | 93 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 8–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 47 | 168 | 122 | inferred_complete_timeline |
| `Action_None` | 178 | 359 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 8–152
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 46 | 39 | inferred_complete_timeline |
| `Action_None` | 47 | 152 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 12–14 | 3 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 69–203 | 67 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 96–170 | 73 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 100–299 | 183 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 102–152 | 51 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 111–179 | 58 | 3 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 117–144 | 22 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 181–311 | 121 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 219–304 | 86 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 224–237 | 14 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 235–338 | 104 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 286–359 | 74 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `13` (C): Annotated start 50 != Inferred start 60
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
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

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [47–59], lower_priority='Action_ZoneBlock' annotated_start=50, effective_Action_ZoneBlock_start=60.
- ⚠️ Action 'Action_None' range [119-153] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-93] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-258] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-168] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-282] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [50-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 119, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [119-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-129] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-169] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-247] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-14] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-203] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-106] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-170] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-299] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-144] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-311] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-304] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-338] for track '26' has 1 frames without a visible bounding box.
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

</details>
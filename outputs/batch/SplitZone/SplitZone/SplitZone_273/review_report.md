# Play-Annotation-Generator Annotation Review — SplitZone_273

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_273`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 135
- **Validation Warnings:** 155
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | Team_Unknown | `13` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 64 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 66 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `7` | 61 | START | 61 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `9` | `9` | 64 | START | 64 | 68 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `11` | `11` | 69 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `14` | `14` | 69 | START | 69 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 69 | START | 69 | 100 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 69 | START | 69 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `7` | `7` | 69 | START | 73 | 85 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 72 | END | 61 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | `13` | `13` | 76 | START | 76 | 79 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 98 | START | 98 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `7` | `7` | 111 | START | 111 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `8` | 112 | START | 112 | 131 |

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
- **Visible Frames:** 0–145
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_SnapReceive` | 61 | 72 | 12 | inferred_complete_timeline |
| `Action_None` | 73 | 97 | 25 | inferred_complete_timeline |
| `Action_Handoff` | 98 | 111 | 14 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 131 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 133 | 145 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SplitBlock` | 64 | 68 | 5 | inferred_complete_timeline |
| `Action_SplitBlock` | 71 | 108 | 38 | inferred_complete_timeline |
| `Action_None` | 109 | 198 | 90 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |
| `Action_None` | 209 | 227 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 118 | 50 | inferred_complete_timeline |
| `Action_None` | 119 | 121 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_BallSnap` | 61 | 72 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 73 | 85 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 163 | 17 | inferred_complete_timeline |
| `Action_None` | 166 | 234 | 69 | inferred_complete_timeline |
| `Action_None` | 241 | 297 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 66–231
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 66 | 68 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 90 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 96 | 105 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 118 | 8 | inferred_complete_timeline |
| `Action_None` | 119 | 184 | 66 | inferred_complete_timeline |
| `Action_None` | 186 | 201 | 16 | inferred_complete_timeline |
| `Action_None` | 208 | 231 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 100 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 104 | 118 | 15 | inferred_complete_timeline |
| `Action_None` | 119 | 184 | 66 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 144 | 84 | inferred_complete_timeline |
| `Action_None` | 154 | 182 | 29 | inferred_complete_timeline |
| `Action_None` | 185 | 280 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 53 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 60 | 2 | inferred_complete_timeline |
| `Action_None` | 61 | 64 | 4 | inferred_complete_timeline |
| `Action_None` | 68 | 101 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–289
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 76 | 16 | inferred_complete_timeline |
| `Action_None` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 197 | 16 | inferred_complete_timeline |
| `Action_None` | 201 | 208 | 8 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 215 | 289 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 79 | 19 | inferred_complete_timeline |
| `Action_None` | 103 | 110 | 8 | inferred_complete_timeline |
| `Action_None` | 127 | 160 | 34 | inferred_complete_timeline |
| `Action_None` | 163 | 202 | 40 | inferred_complete_timeline |
| `Action_None` | 212 | 295 | 84 | inferred_complete_timeline |
| `Action_None` | 301 | 359 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 135 | 75 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 170 | 192 | 23 | inferred_complete_timeline |
| `Action_None` | 194 | 359 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_None` | 61 | 119 | 59 | inferred_complete_timeline |
| `Action_None` | 125 | 157 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 21 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_None` | 73 | 77 | 5 | inferred_complete_timeline |
| `Action_None` | 88 | 92 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 54–297 | 200 | 10 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 94–208 | 44 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 98–299 | 197 | 2 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 104–138 | 35 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 104–158 | 55 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 111–208 | 70 | 4 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 112–336 | 222 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 139–353 | 189 | 3 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 155–210 | 48 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 168–359 | 163 | 6 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 173–189 | 17 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 173–312 | 140 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 177–359 | 177 | 4 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 201–301 | 99 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 205–359 | 130 | 7 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 211–359 | 146 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 268–300 | 33 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 289–292 | 4 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 299–359 | 61 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 304–359 | 56 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 310–359 | 50 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `9` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `11` (LG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `13` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 110 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [61–72], lower_priority='Action_ZoneBlock' annotated_start=69, effective_Action_ZoneBlock_start=73.
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=69, end=64. Clamping end to start.
- ⚠️ Action 'Action_None' range [61-79] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-202] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-295] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-76] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-197] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-289] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-184] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-157] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-192] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-144] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-280] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 119, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [119-121] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [73-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [87-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [103-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-107] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [111-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [123-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-234] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-297] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-131] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [133-145] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [64-68] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-227] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-53] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-58] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-63] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [76-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [85-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [104-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-257] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-281] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-297] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-90] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [96-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-184] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-284] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-158] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-208] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-274] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-336] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-218] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-338] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-192] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-214] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-226] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-272] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-189] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-312] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-293] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-301] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-218] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-306] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-268] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-304] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-300] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>
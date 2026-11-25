# Play-Annotation-Generator Annotation Review — InsideZoneRead_267

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_267`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 117
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ EXACT | `Action_BallSnap` | SAF2 | defense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | DE1 | defense | `9` | `8` |
| ✅ EXACT | `Action_ReadDefender` | DE1 | defense | `9` | `8` |
| ✅ EXACT | `Action_Keep` | DE1 | defense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | defense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_BallSnap` | SAF2 | `10` | `9` | 1 | START | 1 | 13 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `11` | 4 | START | 4 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `14` | 4 | START | 4 | 78 |
| ✅ EXACT | `Action_ZoneBlock` | C | `18` | `17` | 4 | START | 4 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `20` | 4 | START | 4 | 29 |
| ✅ EXACT | `Action_SnapReceive` | DE1 | `9` | `8` | 13 | END | 1 | 13 |
| ✅ EXACT | `Action_ReadDefender` | DE1 | `9` | `8` | 17 | START | 17 | 24 |
| ✅ EXACT | `Action_Keep` | DE1 | `9` | `8` | 25 | START | 25 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DE1 | `9` | `8` | 44 | START | 44 | 95 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 80 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 38 | 38 | inferred_complete_timeline |
| `Action_None` | 45 | 258 | 214 | inferred_complete_timeline |
| `Action_None` | 260 | 263 | 4 | inferred_complete_timeline |
| `Action_None` | 267 | 272 | 6 | inferred_complete_timeline |
| `Action_None` | 282 | 299 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 119 | 119 | inferred_complete_timeline |
| `Action_None` | 123 | 230 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 107 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 64 | 64 | inferred_complete_timeline |
| `Action_None` | 69 | 92 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 78 | 75 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 80 | 1 | inferred_complete_timeline |
| `Action_None` | 81 | 104 | 24 | inferred_complete_timeline |
| `Action_None` | 115 | 135 | 21 | inferred_complete_timeline |
| `Action_None` | 138 | 144 | 7 | inferred_complete_timeline |
| `Action_None` | 164 | 242 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 77 | 74 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 109 | 299 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 44 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 4 | 29 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 50 | 80 | 31 | inferred_complete_timeline |
| `Action_None` | 81 | 270 | 190 | inferred_complete_timeline |
| `Action_None` | 272 | 286 | 15 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–128
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_SnapReceive` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_None` | 14 | 16 | 3 | inferred_complete_timeline |
| `Action_ReadDefender` | 17 | 24 | 8 | inferred_complete_timeline |
| `Action_Keep` | 25 | 43 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 44 | 95 | 52 | inferred_complete_timeline |
| `Action_BallCarry` | 127 | 128 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 68 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 39 | 39 | inferred_complete_timeline |
| `Action_None` | 90 | 299 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 224 | 224 | inferred_complete_timeline |
| `Action_None` | 227 | 299 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 156 | 156 | inferred_complete_timeline |
| `Action_None` | 162 | 299 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 299 | 299 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 235 | 235 | inferred_complete_timeline |
| `Action_None` | 237 | 240 | 4 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 199 | 199 | inferred_complete_timeline |
| `Action_None` | 204 | 299 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_BallSnap` | 1 | 13 | 13 | inferred_complete_timeline |
| `Action_None` | 14 | 242 | 229 | inferred_complete_timeline |
| `Action_None` | 245 | 252 | 8 | inferred_complete_timeline |
| `Action_None` | 260 | 299 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–251 | 216 | 6 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 19–299 | 208 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 40–298 | 226 | 7 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 79–80 | 2 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 87–89 | 3 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 112–202 | 91 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 117–299 | 183 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 121–299 | 130 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 124–146 | 16 | 2 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 146–196 | 42 | 5 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 158–169 | 11 | 2 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 163–299 | 137 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 163–169 | 7 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 182–185 | 4 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 197–240 | 19 | 3 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 211–212 | 2 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 214–299 | 86 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 243–299 | 54 | 4 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 269–299 | 31 | 1 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 534: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [1-107] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-224] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-156] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-235] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [44-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [127-128] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-242] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-119] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-44] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-258] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-78] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-104] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-135] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-144] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-242] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-148] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-251] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-77] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-68] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [4-29] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-270] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-286] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [19-20] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-34] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-77] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-72] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-89] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-237] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-298] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-136] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-154] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-170] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-196] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-165] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-169] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-185] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-237] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-277] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-290] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_267'; source metadata written as null.

</details>
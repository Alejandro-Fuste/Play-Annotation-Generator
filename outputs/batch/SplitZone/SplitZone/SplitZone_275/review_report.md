# Play-Annotation-Generator Annotation Review — SplitZone_275

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `SplitZone_275`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 106
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 7
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `2` | `2` |
| ✅ EXACT | `Action_Handoff` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT2 | defense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `0` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `18` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `2` | `Group` | 0 | START | 0 | 113 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 110 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 98 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `8` | 99 | START | 99 | 106 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `16` | `16` | 106 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `13` | `13` | 111 | START | 111 | 127 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `14` | 111 | START | 111 | 115 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `15` | 111 | START | 111 | 124 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `17` | 111 | START | 111 | 121 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `5` | `5` | 111 | START | 111 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `8` | `8` | 111 | START | 111 | 150 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `2` | `2` | 114 | START | 114 | 157 |
| ✅ EXACT | `Action_Handoff` | LG | `17` | `17` | 122 | START | 122 | 124 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `15` | `15` | 125 | START | 125 | 131 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LG | `17` | `17` | 125 | START | 125 | 169 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT2 | `6` | `6` | 145 | START | 150 | 215 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 56 | 9 | inferred_complete_timeline |
| `Action_None` | 113 | 145 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_PressEdge` | 111 | 127 | 17 | inferred_complete_timeline |
| `Action_PressEdge` | 138 | 154 | 17 | inferred_complete_timeline |
| `Action_None` | 155 | 243 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 143 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 124 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_SplitBlock` | 114 | 157 | 44 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 214 | 36 | inferred_complete_timeline |
| `Action_None` | 221 | 299 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–228
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 122 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 135 | 12 | inferred_complete_timeline |
| `Action_ZoneBlock` | 137 | 154 | 18 | inferred_complete_timeline |
| `Action_None` | 155 | 156 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 162 | 3 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 110 | 64 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 121 | 11 | inferred_complete_timeline |
| `Action_Handoff` | 122 | 124 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 125 | 169 | 45 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 181 | 197 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_BallSnap` | 99 | 106 | 8 | inferred_complete_timeline |
| `Action_None` | 107 | 110 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 150 | 40 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 155 | 299 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 124 | 14 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 125 | 131 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 142 | 188 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 110 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 122 | 127 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 152 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 178 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 140 | 42 | inferred_complete_timeline |
| `Action_None` | 145 | 154 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 212 | 114 | inferred_complete_timeline |
| `Action_None` | 220 | 242 | 23 | inferred_complete_timeline |
| `Action_None` | 245 | 277 | 33 | inferred_complete_timeline |
| `Action_None` | 279 | 281 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_BallCarry` | 150 | 215 | 66 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 299 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 220 | 122 | inferred_complete_timeline |
| `Action_None` | 224 | 284 | 61 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 260 | 162 | inferred_complete_timeline |
| `Action_None` | 263 | 299 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 172 | 74 | inferred_complete_timeline |
| `Action_None` | 179 | 299 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 165 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 129–165 | 24 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 131–299 | 169 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 137–138 | 2 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 151–279 | 129 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 157–164 | 8 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 171–186 | 16 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 172–266 | 87 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 173–277 | 95 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 182–269 | 47 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 188–260 | 73 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 197–299 | 103 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 198–283 | 62 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 206–276 | 54 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 211–220 | 10 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 242–244 | 3 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 273–289 | 17 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `16` (QB)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BlockSecondLevel' at frame 125 targets track ID '150', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 69 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [99-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-260] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-214] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-284] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-122] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-135] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-139] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [150-215] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-299] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-242] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-277] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-140] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-178] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [111-127] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [138-154] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-243] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [111-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [122-127] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-152] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [125-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [142-188] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-56] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-145] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [125-169] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [181-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-143] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-146] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-186] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-182] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-266] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-261] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-277] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-269] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-260] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-205] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-279] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-267] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-220] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-289] for track '35' has 2 frames without a visible bounding box.
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

</details>
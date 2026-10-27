# Play-Annotation-Generator Annotation Review — Counter_299

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_299`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `8` | `7` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `3` | `2` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `18` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 93 |
| ✅ EXACT | `Action_BallSnap` | C | `8` | `7` | 94 | START | 94 | 107 |
| ✅ EXACT | `Action_DownBlock` | RT | `10` | `9` | 97 | START | 97 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `8` | `7` | 97 | START | 108 | 115 |
| ✅ EXACT | `Action_PullBlock` | LG | `19` | `18` | 97 | START | 97 | 179 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `3` | `2` | 97 | START | 97 | 175 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `18` | `17` | 105 | START | 105 | 125 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 107 | END | 94 | 107 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 124 | START | 124 | 139 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `18` | `17` | 140 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 179 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_SnapReceive` | 94 | 107 | 14 | inferred_complete_timeline |
| `Action_None` | 108 | 123 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 124 | 139 | 16 | inferred_complete_timeline |
| `Action_None` | 140 | 214 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 105 | 125 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 359 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 244 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 246 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–246
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 97 | 175 | 79 | inferred_complete_timeline |
| `Action_None` | 184 | 246 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 141 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PullBlock` | 97 | 179 | 83 | inferred_complete_timeline |
| `Action_None` | 180 | 204 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_BallSnap` | 94 | 107 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 108 | 115 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 179 | 47 | inferred_complete_timeline |
| `Action_None` | 180 | 359 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 113 | 20 | inferred_complete_timeline |
| `Action_None` | 115 | 133 | 19 | inferred_complete_timeline |
| `Action_None` | 141 | 271 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 256

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_DownBlock` | 97 | 179 | 83 | inferred_complete_timeline |
| `Action_None` | 180 | 255 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–271
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 169 | 76 | inferred_complete_timeline |
| `Action_None` | 178 | 188 | 11 | inferred_complete_timeline |
| `Action_None` | 190 | 271 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 201 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 131 | 38 | inferred_complete_timeline |
| `Action_None` | 133 | 223 | 91 | inferred_complete_timeline |
| `Action_None` | 225 | 328 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 148 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–342
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 226 | 133 | inferred_complete_timeline |
| `Action_None` | 228 | 276 | 49 | inferred_complete_timeline |
| `Action_None` | 312 | 342 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 258 | 165 | inferred_complete_timeline |
| `Action_None` | 261 | 267 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 257 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 319 | 226 | inferred_complete_timeline |
| `Action_None` | 321 | 322 | 2 | inferred_complete_timeline |
| `Action_None` | 332 | 354 | 23 | inferred_complete_timeline |
| `Action_None` | 357 | 358 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 249 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_None` | 94 | 212 | 119 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_None` | 219 | 223 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 66 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 69 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 85 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_None` | 94 | 138 | 45 | inferred_complete_timeline |
| `Action_None` | 144 | 150 | 7 | inferred_complete_timeline |
| `Action_None` | 152 | 257 | 106 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 33–34 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 42–44 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 59–63 | 4 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 122–277 | 148 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 130–246 | 115 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 154–245 | 92 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 186–226 | 19 | 5 | Undefined position; Undefined team |
| `29` | `30` | Position_Unknown | Team_Unknown | 192–207 | 13 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 243–244 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 259–359 | 101 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 261–272 | 12 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 275–359 | 85 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 287–359 | 73 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 300–359 | 60 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 313–359 | 47 | 1 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 349–359 | 11 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 349–359 | 10 | 2 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 350–359 | 10 | 1 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 357–359 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `18` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `22`): `SAF2` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [94–107], lower_priority='Action_DownBlock' annotated_start=97, effective_Action_DownBlock_start=108.
- ⚠️ Segment 'Action_BallCarry' for track '17' has invalid range: start=140, end=125. Clamping end to start.
- ⚠️ Action 'Action_None' range [94-244] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-169] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-188] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-271] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [97-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-131] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-328] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [108-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-319] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-354] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-255] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-249] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-258] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-267] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-212] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-113] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-133] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-271] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [105-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-204] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-276] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-342] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-138] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-257] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-44] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-277] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-243] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-245] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-193] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-207] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-272] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-359] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-354] for track '38' has 1 frames without a visible bounding box.
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

</details>
# Play-Annotation-Generator Annotation Review — Dagger_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_9`
- **Frame Range:** 0 to 388 (389 total frames)
- **Play:** `Play_Unknown`
- **Result:** `Result_Unknown`
- **Result Frame:** 388
- **Player Tracks:** 32
- **Ball Tracks:** 2
- **Action Segments:** 60
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 0
- **Exact Matches:** 0
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

*(No offensive player tracks)*

</details>

<details>
<summary><strong>Defense</strong></summary>

*(No defensive player tracks)*

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–327 | 327 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–238 | 239 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–359 | 360 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–344 | 319 | 7 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–240 | 240 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–267 | 267 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–388 | 381 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–170 | 171 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–333 | 333 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–28 | 29 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–150 | 151 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–303 | 302 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–388 | 389 | 1 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–375 | 376 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–323 | 311 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–202 | 199 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–212 | 213 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 2–254 | 248 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 48–84 | 37 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 84–337 | 253 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 87–228 | 142 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 184–388 | 202 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 203–291 | 89 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 211–388 | 165 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 214–348 | 131 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 259–285 | 25 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 278–368 | 87 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 285–388 | 95 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 290–295 | 6 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 304–388 | 85 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 313–384 | 72 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 319–388 | 70 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `25` | `29` | 223 | 229 | 6 | 85.7% | 226 |
| `31` | `41` | 308 | 308 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 55 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 388 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-327] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-238] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-309] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-314] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-321] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-338] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-344] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [113-267] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-369] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-333] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-303] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-388] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-375] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-203] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-323] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-90] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-254] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-261] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-337] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-388] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-291] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-223] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-313] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-323] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-324] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-348] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-269] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-285] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-361] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-368] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-350] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-364] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-384] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_Unknown'.

</details>
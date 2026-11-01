# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_172`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_172/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [32–48], lower_priority='Action_ZoneBlock' annotated_start=35, effective_Action_ZoneBlock_start=49.
> - Action 'Action_None' range [32-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-253] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-295] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-316] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-63] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-272] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-107] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-87] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [73-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-201] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-309] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-300] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-92] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-301] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-54] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-132] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-147] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-221] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-53] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-91] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-304] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-322] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-61] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-274] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-137] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-196] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-244] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-183] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-199] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-307] for track '35' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
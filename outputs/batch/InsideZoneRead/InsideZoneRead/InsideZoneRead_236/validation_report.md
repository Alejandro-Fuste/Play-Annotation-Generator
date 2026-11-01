# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_236`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_236/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [11–26], lower_priority='Action_ZoneBlock' annotated_start=14, effective_Action_ZoneBlock_start=27.
> - Action 'Action_None' range [11-141] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-158] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-88] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-81] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-133] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [54-58] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [60-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-145] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-177] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-52] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-79] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [11-24] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-169] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-70] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-149] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [103-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '20' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
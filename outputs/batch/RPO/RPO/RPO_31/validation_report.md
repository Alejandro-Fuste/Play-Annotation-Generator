# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_31`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LG) duration 92 frames exceeds threshold 90 frames [start=44, end=135].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 92 frames exceeds threshold 90 frames [start=44, end=135].
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (LT) duration 92 frames exceeds threshold 90 frames [start=44, end=135].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 92 frames exceeds threshold 90 frames [start=44, end=135].
> - Action 'Action_None' range [43-319] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-119] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-67] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-98] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-86] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-181] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-111] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-265] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-170] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-308] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-329] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-53] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-65] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-63] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-71] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-246] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-140] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-313] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-156] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-144] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-187] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-305] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-325] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-327] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
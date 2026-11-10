# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_40`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_40/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [51-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-275] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-286] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-259] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-278] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-121] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [123-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-139] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-288] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [51-140] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-246] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-299] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [51-234] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-255] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-112] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-151] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-112] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-75] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-82] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-108] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-299] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [57-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [92-105] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-64] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-65] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-20] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-78] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-105] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-143] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-222] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-218] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
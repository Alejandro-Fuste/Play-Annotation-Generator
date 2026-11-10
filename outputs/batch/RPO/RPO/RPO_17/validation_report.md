# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_17`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [39-62] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-186] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-206] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-236] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-263] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-274] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-163] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-283] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-299] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-57] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-93] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-182] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-297] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-109] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-215] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-279] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-44] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-285] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-47] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '15' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-38] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-95] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-290] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-153] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-214] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-182] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-273] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-277] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-255] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-267] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-248] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-258] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-294] for track '31' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_32`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PressEdge' range [94-113] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-193] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-299] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-141] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-290] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-232] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-181] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-295] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-177] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-266] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-158] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-299] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-200] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-299] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-223] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-227] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-245] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-264] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-242] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-298] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
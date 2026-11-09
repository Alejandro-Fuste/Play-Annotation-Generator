# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_188`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_188/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 37 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-97] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-151] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-87] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-140] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-122] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-259] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-289] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_Keep' range [70-211] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-220] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-200] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-213] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-227] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-251] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-265] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-299] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-259] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-270] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-288] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-282] for track '36' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
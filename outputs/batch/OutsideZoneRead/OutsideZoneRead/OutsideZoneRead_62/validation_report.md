# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_62`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_62/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [144-204] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-173] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-188] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-231] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [116-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-143] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-262] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-235] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-244] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-252] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-280] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-184] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [144-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-143] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-155] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-211] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-130] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-152] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-279] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-186] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-190] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-220] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-230] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-241] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-260] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-295] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-276] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-288] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-286] for track '33' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
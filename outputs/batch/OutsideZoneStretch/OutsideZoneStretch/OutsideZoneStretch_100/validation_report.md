# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_100`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_100/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 202: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [83-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-151] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-194] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-139] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-34] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-89] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-106] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-149] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-169] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-207] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-143] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-91] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-167] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-193] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-23] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-104] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-152] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-162] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-75] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-45] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-124] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-27] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-54] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-47] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-66] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-58] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-88] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-123] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-137] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-177] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-106] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-132] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-148] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-156] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-169] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-169] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-181] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-196] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-195] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-201] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-208] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-199] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-210] for track '39' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
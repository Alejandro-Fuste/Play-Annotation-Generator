# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_7`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_7/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 16: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [118-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-170] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-147] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-246] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-248] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-257] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-240] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-297] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [77-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-125] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-226] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-329] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-25] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-113] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-176] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-244] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-102] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-103] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-160] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-235] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-187] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-160] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-311] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-224] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-238] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-329] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-197] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-236] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-228] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-282] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-230] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-311] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-317] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-327] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-308] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-286] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-293] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-286] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-304] for track '37' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
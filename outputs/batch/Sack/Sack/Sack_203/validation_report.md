# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_203`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_203/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-79] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-265] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-272] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-282] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-135] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-240] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-261] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-266] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-283] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-286] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-293] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-110] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-144] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-83] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-14] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [110-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-294] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-262] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-289] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-108] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-270] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-273] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-286] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-290] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-294] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-264] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-274] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-284] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-267] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-252] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-260] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-275] for track '21' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
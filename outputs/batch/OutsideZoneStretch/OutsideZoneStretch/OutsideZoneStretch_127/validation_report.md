# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_127`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_127/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-222] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-298] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-146] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-279] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-189] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-189] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-74] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-254] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-251] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-115] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [116-179] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-299] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-76] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-88] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-149] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-272] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-255] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-205] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-258] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-251] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-284] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-233] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-264] for track '28' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
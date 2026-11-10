# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_23`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 25, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '180,193;?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-160] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-119] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [132-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [181-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-148] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-198] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [132-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [155-160] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [163-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-164] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-172] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-130] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-177] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [132-152] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [154-192] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [207-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-10] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-22] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-32] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-41] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-49] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-118] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-178] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-187] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-164] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-191] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-198] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-203] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-198] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-210] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-193] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-196] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-210] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '33' has 1 frames without a visible bounding box.
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
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.
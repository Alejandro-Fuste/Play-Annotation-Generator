# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_25`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_25/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 147 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 93 frames exceeds threshold 90 frames [start=102, end=194].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 102 frames exceeds threshold 90 frames [start=102, end=203].
> - Validation warning: Action 'Action_ZoneBlock' for track '16' (C) duration 102 frames exceeds threshold 90 frames [start=102, end=203].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [99–116], lower_priority='Action_ZoneBlock' annotated_start=102, effective_Action_ZoneBlock_start=117.
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (LT) duration 102 frames exceeds threshold 90 frames [start=102, end=203].
> - Action 'Action_None' range [99-144] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-194] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-151] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-166] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-183] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-206] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-112] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-151] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-164] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-257] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-223] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-279] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [281-328] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-293] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-318] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-330] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-339] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-98] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-144] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-340] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-336] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-340] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [105-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-359] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-228] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [190-194] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 204, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [204-359] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [117-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [131-161] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [163-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-168] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [186-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [126-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [102-118] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [131-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-146] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [170-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-293] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-359] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-346] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-146] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [179-182] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-6] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-359] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-228] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-314] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-203] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-219] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-233] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-248] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-223] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-266] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-219] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-236] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [242-359] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-262] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-263] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [265-268] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-331] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [336-339] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-356] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-285] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-350] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [353-355] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-358] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-326] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-327] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [344-349] for track '42' has 1 frames without a visible bounding box.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.